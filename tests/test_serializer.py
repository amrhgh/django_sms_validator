from .conftest import pytest_configure
from sms_validator.models import PhoneCode

from django.test import TestCase
from sms_validator.serializers import PhoneCodeSerializer
from sms_validator.utils import code_generation


class TestSerializer(TestCase):
    def setUp(self):
        self.phone_number = '09000000000'
        self.code = code_generation()

    def test_it_not_should_be_validate_if_fields_messing(self):
        obj = PhoneCodeSerializer(data={})
        self.assertFalse(obj.is_valid())
        self.assertIn('phone_number', obj.errors)
        self.assertIn('code', obj.errors)
        obj = PhoneCodeSerializer(data={'phone_number': self.phone_number})
        self.assertFalse(obj.is_valid())
        self.assertIn('code', obj.errors)
        obj = PhoneCodeSerializer(data={'code': self.code})
        self.assertFalse(obj.is_valid())
        self.assertIn('phone_number', obj.errors)

    def test_serializer_save_data(self):
        obj = PhoneCodeSerializer(data={'phone_number': self.phone_number,
                                        'code': self.code})
        self.assertTrue(obj.is_valid())
        obj.save()
        self.assertEqual(PhoneCode.objects.count(), 1)

    def test_update_code(self):
        obj = PhoneCodeSerializer(data={'phone_number': self.phone_number,
                                        'code': self.code})
        obj.is_valid()
        obj.save()
        phone_code = PhoneCode.objects.get(phone_number=self.phone_number)
        second_code = code_generation()
        obj = PhoneCodeSerializer(phone_code, data={'code': second_code}, partial=True)
        obj.is_valid()
        obj.save()
        phone_code = PhoneCode.objects.get(phone_number=self.phone_number)
        self.assertEqual(phone_code.code, second_code)
