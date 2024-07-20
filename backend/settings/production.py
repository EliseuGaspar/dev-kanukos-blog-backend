from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*.com']

# Configurações de email para produção
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.*-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'eliseugaspar4@gmail.com'
EMAIL_HOST_PASSWORD = '---'
