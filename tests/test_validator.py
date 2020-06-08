from rest_framework.response import Response

from .conftest import pytest_configure
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.test import APIRequestFactory

from sms_validator.serializers import PhoneCodeSerializer
from sms_validator.validator import sms_validator
from django.test import TestCase

from sms_validator.utils import code_generation


class ViewWithSMSValidator(CreateAPIView):
    serializer_class = PhoneCodeSerializer

    @sms_validator
    def create(self, request, *args, **kwargs):
        return Response('OK')


class ValidatorTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.phone_number = '09000000000'
        self.code = code_generation()
        self.view = ViewWithSMSValidator.as_view()

    def test_if_required_field_not_found(self):
        data = {'code': self.code}
        request = self.factory.post('send_sms/', data=data, format='json')
        self.assertEqual(self.view(request).status_code, 400)
        data = {'phone_number': self.phone_number}
        request = self.factory.post('send_sms/', data=data, format='json')
        self.assertEqual(self.view(request).status_code, 400)

    def test_if_phone_code_entity_not_exist(self):
        data = {'phone_number': self.phone_number, 'code': self.code}
        request = self.factory.post('send_sms/', data=data, format='json')
        self.assertEqual(self.view(request).status_code, 400)

    def test_if_phone_code_entity_exist(self):
        data = {'phone_number': self.phone_number, 'code': self.code}
        obj = PhoneCodeSerializer(data=data)
        obj.is_valid()
        obj.save()
        request = self.factory.post('send_sms/', data=data, format='json')
        self.assertEqual(self.view(request).status_code, 200)
        data = {'phone_number': self.phone_number, 'code': '00000'}
        request = self.factory.post('send_sms/', data=data, format='json')
        self.assertEqual(self.view(request).status_code, 400)

