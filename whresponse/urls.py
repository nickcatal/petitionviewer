"""
whresponse URL Configuration
"""
# pylint: disable=invalid-name
from django.conf.urls import include, url
from django.contrib import admin

from responses.views import ResponseListView, ResponseDetailView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ResponseListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/', ResponseDetailView.as_view(), name='response'),
]
