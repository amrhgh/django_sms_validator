from .conftest import pytest_configure
import kavenegar
from rest_framework.test import APIRequestFactory

from sms_validator.serializers import PhoneCodeSerializer
from sms_validator.settings import api_settings
from sms_validator.utils import code_generation
from sms_validator.views import SendSMSView
from django.test import TestCase


class TestSendSMS(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SendSMSView.as_view()
        self.code = code_generation()
        self.phone_number = '09000000000'
        code = code_generation()
        phone_number = '09000000000'
        self.data = {'phone_number': phone_number, 'code': code}
        self.request = self.factory.post('send_sms/', data=self.data, format='json')

    def test_return_500_code_error_when_token_not_found(self):
        sms_config = api_settings
        sms_config.pop('KAVENEGAR_TOKEN')
        self.settings(SMS_VALIDATOR=sms_config)
        response = self.view(self.request)
        self.assertEqual(response.status_code, 500)

    def test_send_sms_view(self):
        sms_config = api_settings
        sms_config['KAVENEGAR_TOKEN'] = 'token'
        self.settings(SMS_VALIDATOR=sms_config)
        with self.assertRaises(kavenegar.APIException):  # I don't have valid token now
            self.view(self.request)

    def test_prevent_send_continuous_sms(self):
        sms_config = api_settings
        sms_config['KAVENEGAR_TOKEN'] = 'token'
        self.settings(SMS_VALIDATOR=sms_config)
        obj = PhoneCodeSerializer(data={'phone_number': self.phone_number,
                                        'code': self.code})
        obj.is_valid()
        obj.save()
        response = self.view(request=self.request)
        self.assertEqual(response.status_code, 405)

