"""
Django settings for myCommServer project.
Generated by 'django-admin startproject' using Django 1.8.13.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dotenv
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# load environment variables from .env
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

'''
    The left hand side will be referenced in python via, e.g.
    from hello import settings
    settings.TWO1_WALLET_MNEMONIC
    The quoted string on the right hand side is the name of the environment
    variable that is loaded by the dotenv package.
'''
rockBlockUsername = "vikaspunia50@gmail.com"
rockBlockPassword = "Vikaspunia@009"
iridiumApi = "https://core.rock7.com/rockblock/MT"
SECRET_KEY = "44wrc^&^@1nbd!-87he#eu6y%(z31)qcxn_7ezn2vbgalm@xe_"
DEBUG = os.environ.get("DEBUG")
GOOGLE_API_KEY = "AIzaSyAChYf5Rs1iR0PpCFkj9i4UazBzAFWhCMs"

# load database from the DATABASE_URL environment variable
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


ALLOWED_HOSTS = ['comnserver.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'myCommServer',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
DEBUG = True

ROOT_URLCONF = 'myCommServer.urls'

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

WSGI_APPLICATION = 'myCommServer.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

