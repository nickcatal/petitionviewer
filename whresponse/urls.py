from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from whresponse.responses.views import ResponseListView, ResponseDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ResponseListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/', ResponseDetailView.as_view(), name='response'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )