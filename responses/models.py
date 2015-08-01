"""Models for responses app"""
from django.db import models


class WhitehouseAbstractModel(models.Model):
    title = models.CharField(max_length=250)
    url = models.CharField(verbose_name=u'Whitehouse URL', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True

    @property
    def official_url(self):
        return "https://petitions.whitehouse.gov{url}".format(
            url=self.url)

    def __unicode__(self):
        return self.title


class Response(WhitehouseAbstractModel):
    slug = models.SlugField(max_length=250)
    total_signatures = models.IntegerField(verbose_name=u'Total Signatures')
    response = models.TextField(verbose_name=u'Full White House Response')

    class Meta(object):
        ordering = ["-created_at", "-total_signatures"]
        verbose_name = ('Response')
        verbose_name_plural = ('Responses')



class Petition(WhitehouseAbstractModel):
    response = models.ForeignKey(Response)
    signatures = models.IntegerField()

    class Meta(object):
        ordering = ["created_at", "-signatures"]
        verbose_name = ('Petition')
        verbose_name_plural = ('Petitions')
