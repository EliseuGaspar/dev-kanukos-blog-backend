from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'backend.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'