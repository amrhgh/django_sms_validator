from setuptools import setup, find_packages

setup(
    author='amirhossein gholamian',
    author_email='amirhgholamian78@gmail.com',
    url='https://github.com/amrhgh/django_sms_validator',
    name="django_rest_sms_validator",
    description='A validator plugin based on sms and uses kavenegar api',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    version="0.1",
    packages=['django_rest_sms_validator', ],
    install_requires=[
        'django=>2.2',
        'djangorestframework',
        'kavenegar=>1.1.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)