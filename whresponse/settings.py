import dj_database_url
from os import environ
from sys import exc_info

from unipath import FSPath as Path

# Helper lambda for gracefully degrading env variables. Taken from http://rdegges.com/devops-django-part-3-the-heroku-way
env = lambda e, d: environ[e] if environ.has_key(e) else d

BASE = Path(__file__).absolute().ancestor(2)
APP = Path(__file__).absolute().ancestor(1)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost'),
}

if environ.has_key('AK_DBUSER'):
    DATABASES['actionkit'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ['AK_DBNAME'],
        'USER': environ['AK_DBUSER'],
        'PASSWORD': environ['AK_DBPASS'],
        'HOST': env('AK_DBSERVER','client-db.actionkit.com'),
        'PORT': '3306',
    }

ALLOWED_HOSTS = []

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

if environ.has_key('AWS_STORAGE_BUCKET'):
    AWS_STORAGE_BUCKET_NAME = environ['AWS_STORAGE_BUCKET']
    AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_ACCESS_KEY']
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
else:
    STATIC_URL = '/static/'

# Additional locations of static files
MEDIA_ROOT = BASE.child('media')
STATIC_ROOT = BASE.child('static')
STATICFILES_DIRS = (
    BASE.child('ui'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env('SECRET_KEY', 'fawefawief123123bnqawf123j253blrq1231l23ubqwfawelu123')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whresponse.middleware.DisableStaffCachingMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'whresponse.urls'

TEMPLATE_DIRS = [APP.child('templates')]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Enable Django Admin
    'django.contrib.admin',

    # Heroku Specific Apps Here
    'gunicorn',

    # 3rd Party
    'storages',
    'boto',
    'south',

    # 1st Party Apps
    'whresponse.responses'


)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-location'
    }
}

CACHE_MIDDLEWARE_SECONDS = 3600

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Import from localsettings
try:
    from whresponse.localsettings import *
except ImportError:
    pass