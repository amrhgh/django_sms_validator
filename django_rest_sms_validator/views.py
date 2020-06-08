import datetime

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from django_rest_sms_validator.models import PhoneCode
from django_rest_sms_validator.serializers import PhoneCodeSerializer
from django_rest_sms_validator.settings import api_settings
from django_rest_sms_validator.utils import send_sms_kavenegar


class SendSMSView(CreateAPIView):
    """
    this class used for send sms code to given phone number
    """
    authentication_classes = []
    permission_classes = []
    serializer_class = PhoneCodeSerializer

    def create(self, request, *args, **kwargs):
        token = api_settings.get('KAVENEGAR_TOKEN')
        if not token:
            return Response('at first you should specify your kavenegar token', status=500)
        if not self.check_repeating_sms_limit(request.data['phone_number']):
            return Response('last sms Just sent', status=405)
        self.create_or_update_phone_code(request.data.get('phone_number'), request.data.get('code'))
        send_sms_response = send_sms_kavenegar(token=token, **request.data)
        return Response(send_sms_response)

    def create_or_update_phone_code(self, phone_number, code):
        """
        create new phone code entity if phone code record doesn't have exist before
        else just update existed record
        """
        phone_code = PhoneCode.objects.filter(phone_number=phone_number).first()
        if phone_code:
            obj = self.get_serializer(phone_code, data={'code': code}, partial=True)

        else:
            obj = self.get_serializer(data={'phone_number': phone_number,
                                            'code': code})
        obj.is_valid()
        obj.save()
        return obj

    def check_repeating_sms_limit(self, phone_number):
        """
        to prevent sending continuous sms, can set intervals between sms
        """
        obj = PhoneCode.objects.filter(phone_number=phone_number).first()
        if not obj:
            return True
        current_time = datetime.datetime.now()
        expire_time = api_settings['TOKEN_LIFETIME']
        if obj.expire_at < current_time + expire_time:
            return False
        return True
