from datetime import timedelta

from django.conf import settings

USER_SETTINGS = getattr(settings, 'SMS_VALIDATOR', dict())

DEFAULTS = {
    'TOKEN': 'Token given from kavenegar',
    'NEXT_SMS_TIMEOUT': timedelta(seconds=30),
    'TOKEN_LIFETIME': timedelta(minutes=2),
    'PHONE_FIELD_NAME': 'phone_number'
}

api_settings = {**DEFAULTS, **USER_SETTINGS}
