import os
from .base import *  # noqa: F403

DEBUG = True

INSTALLED_APPS.append('django_nose')  # noqa: F405

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    '-s',
    '--nologcapture',
    '--with-coverage',
    '--with-progressive',
    '--cover-package={{cookiecutter.app_name}}'
]

# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
