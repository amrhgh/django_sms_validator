from setuptools import setup, find_packages

setup(
    name="django_rest_sms_validator",
    description='A validator plugin based on sms and uses kavenegar api',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    version="0.1",
    packages=['django_rest_sms_validator',]
)