import random

from kavenegar import KavenegarAPI

from django_rest_sms_validator.settings import api_settings


def code_generation():
    """
    generate random code with five digit
    """
    n = api_settings.get('CODE_LENGTH')
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(random.randint(range_start, range_end))


def send_sms_kavenegar(token, phone_number, code):
    api = KavenegarAPI(token)
    params = {'receptor': phone_number, 'token': code, 'template': 'SymptomCheckerVerify'}
    response = api.verify_lookup(params)
    return response
