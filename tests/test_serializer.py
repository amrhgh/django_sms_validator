from .conftest import pytest_configure

pytest_configure()
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








