"""
WSGI config for whresponse project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whresponse.settings")

# Django whitenoise must be included after DJANGO_SETTINGS_MODULE has been set
from whitenoise.django import DjangoWhiteNoise

# Fix django closing connection to memcached after every request
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
