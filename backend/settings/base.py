""" Aqui encontram-se as configurações base do projeto """
import os
from .base import *
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/storage/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'storage')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'api',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

USE_TZ = True
USE_I18N = True
TIME_ZONE = 'UTC'
STATIC_URL = '/static/'
LANGUAGE_CODE = 'pt-pt'
ROOT_URLCONF = 'backend.urls'
SECRET_KEY = '##--ap1*2l0g--##'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'