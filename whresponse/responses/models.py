from django.db import models

class Response(models.Model):
    slug = models.SlugField(max_length=250)
    title = models.CharField(verbose_name=u'Response Title', max_length=250)
    total_signatures = models.IntegerField(verbose_name=u'Total Signatures')
    response = models.TextField(verbose_name=u'Full White House Response')
    url = models.CharField(verbose_name=u'Whitehouse URL', max_length=250)
    created_at = models.DateTimeField(auto_now = True, auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ["-total_signatures"]
        verbose_name = ('Response')
        verbose_name_plural = ('Responses')

    def __unicode__(self):
        return self.title

class Petition(models.Model):
    response = models.ForeignKey(Response)
    title = models.CharField(verbose_name=u'Petition Title', max_length=250)
    url = models.URLField(verbose_name=u'Petition URL')
    signatures = models.IntegerField()
    created_at = models.DateTimeField(auto_now = True, auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ["-signatures"]
        verbose_name = ('Petition')
        verbose_name_plural = ('Petitions')

    def __unicode__(self):
        return self.title
    