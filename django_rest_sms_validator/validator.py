import datetime

from rest_framework.exceptions import ValidationError

from django_rest_sms_validator.models import PhoneCode
from django_rest_sms_validator.settings import api_settings


def sms_validator(func):
    def wrap(*args, **kwargs):
        code = args[1].data.get('code')
        phone_number = args[1].data.get('phone_number')
        if not code:
            raise ValidationError('code not found')
        if not phone_number:
            raise ValidationError('phone number not found')
        if check_code_correction(phone_number, code):
            return func(*args, **kwargs)
        raise ValidationError('phone number or code is not correct')

    return wrap


def check_code_correction(phone_number, code):
    phone_code = PhoneCode.objects.filter(phone_number=phone_number).first()
    if phone_code:
        current_time = datetime.datetime.now()
        expire_time = api_settings['TOKEN_LIFETIME']
        if phone_code.expire_at > current_time - expire_time:
            return phone_code.code == code
    return False
