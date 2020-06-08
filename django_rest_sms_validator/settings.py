from datetime import timedelta

from django.conf import settings

USER_SETTINGS = getattr(settings, 'SMS_VALIDATOR', dict())

DEFAULTS = {
    'NEXT_SMS_TIMEOUT': timedelta(seconds=30),
    'TOKEN_LIFETIME': timedelta(minutes=2),
}

api_settings = {**DEFAULTS, **USER_SETTINGS}
