import datetime

from rest_framework import serializers

from django_rest_sms_validator.models import PhoneCode
from django_rest_sms_validator.settings import api_settings


class PhoneCodeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        add current time and expire time specified in settings
        :param validated_data: includes phone number and code
        """
        current_time = datetime.datetime.now()
        expire_time = api_settings['TOKEN_LIFETIME']
        if obj := PhoneCode.objects.filter(phone_number=validated_data.get('phone_number')).first():
            obj.created_at = current_time
            obj.expire_at = expire_time
            obj.code = validated_data.get('code')
            obj.update()
        else:
            obj = PhoneCode.objects.create(created_at=current_time, expire_at=current_time + expire_time,
                                           **validated_data)
        return obj

    def update(self, instance, validated_data):
        current_time = datetime.datetime.now()
        expire_time = api_settings['TOKEN_LIFETIME']
        instance.code = validated_data.get('code')
        instance.created_at = current_time
        instance.expire_at = current_time + expire_time
        instance.save()
        return instance

    def validate_phone_number(self, value):
        message = f'{value} is not valid phone number'
        if not value.isnumeric():
            raise serializers.ValidationError(message)
        if len(value) != 11:
            raise serializers.ValidationError(message)
        return value

    class Meta:
        model = PhoneCode
        fields = '__all__'
        read_only_fields = ('created_at', 'expire_at')
