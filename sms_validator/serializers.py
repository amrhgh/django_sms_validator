import datetime

from rest_framework import serializers

from sms_validator.models import PhoneCode
from sms_validator.settings import api_settings


class PhoneCodeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        add current time and expire time specified in settings
        :param validated_data: includes phone number and code
        """
        current_time = datetime.datetime.now()
        expire_time = api_settings['TOKEN_LIFETIME']
        obj = PhoneCode.objects.create(created_at=current_time, expire_at=current_time + expire_time, **validated_data)
        return obj

    class Meta:
        model = PhoneCode
        fields = '__all__'
        read_only_fields = ('created_at', 'expire_at')
