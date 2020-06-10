# django_rest_sms_validator

this package provides a sms validator based on **kavenegar api** for DJANGO REST FRAMEWORK.


### Instalation
after install package with pip : 

1 - add `'django_rest_sms_validator'` to your `INSTALLED_APPS`:

    INSTALLED_APPS = [
        ...
        'django_rest_sms_validator',
    ]
    
2 - add your kavenegar token to settings.py:

    SMS_VALIDATOR= {
        'KAVENEGAR_TOKEN': 'your token'
    }

3 - add send sms view to your `urls.py`:

    from django_rest_sms_validator.views import SendSMSView
    
    urlpatterns = [
        ...
        path('send_sms/', SendSMSView.as_view()),
    ]


### Usage

add `@sms_validator` decorator to views which are wanted to be validate with sms

example:

    class ViewWithSMSValidator(CreateAPIView):

        @sms_validator
        def create(self, request, *args, **kwargs):
            return Response('OK')
            
### configs

    SMS_VALIDATOR = {
        'NEXT_SMS_TIMEOUT': timedelta(seconds=30),
        'TOKEN_LIFETIME': timedelta(minutes=2),
        'CODE_LENGTH': 5
    }
    
NEXT_SMS_TIMEOUT: time limitation between two sms with same phone number

TOKEN_LIFETIME: time period that the token sent is valid.

CODE_LENGTH: length of generated code
    

