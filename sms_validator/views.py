from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from sms_validator.settings import api_settings
from sms_validator.utils import send_sms_kavenegar


class SendSMSView(CreateAPIView):
    """
    this class used for send sms code to given phone number
    """
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        token = api_settings.get('KAVENEGAR_TOKEN')
        if not token:
            return Response('at first you should specify your kavenegar token', status=500)
        send_sms_response = send_sms_kavenegar(token=token, **request.data)
        return Response(send_sms_response)

    # def check_repeating_sms_limit(self, phone_number):
    #     """
    #     to prevent sending continuous sms, can set intervals between sms
    #     """
