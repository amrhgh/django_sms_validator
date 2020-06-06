import random

from kavenegar import KavenegarAPI


def code_generation():
    # TODO: specify length of digits dynamically
    """
    generate random code with five digit
    """
    code = '{0:05}'.format(random.randint(1, 100000))
    return code


def send_sms_kavenegar(token, phone_number, code):
    api = KavenegarAPI(token)
    params = {'receptor': phone_number, 'token': code, 'template': 'SymptomCheckerVerify'}
    response = api.verify_lookup(params)
    return response
