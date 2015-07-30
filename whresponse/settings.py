"""
Django settings for whpetition project.
"""
# pylint: disable=invalid-name
import os

import environ
from memcacheify import memcacheify

root = environ.Path(__file__) - 3
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, [''])
)
environ.Env.read_env('.env')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}

# Attempt to get the memcache info from Heroku.
default_cache = memcacheify()['default']

# memcacheify will use the LocMemCache if there is no heroku cache. So if we
# see the 'LocMemCache' we know that memcachify is not running on a heroku dyno
# that is setup for memcached
if default_cache['BACKEND'] == 'django.core.cache.backends.locmem.LocMemCache':
    default_cache = env.cache()

CACHES = {
    'default': default_cache,
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ui'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'responses'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
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

ROOT_URLCONF = 'whresponse.urls'

WSGI_APPLICATION = 'whresponse.wsgi.application'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


LOGGING = {
    'version': 1,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        }
    },
}
