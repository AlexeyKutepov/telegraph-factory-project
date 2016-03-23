from django.db import models

# Create your models here.

from cms.models.pluginmodel import CMSPlugin

from django.db import models

from filer.fields.image import FilerImageField


class Portfolio(CMSPlugin):
    image = FilerImageField()
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.header

    def __unicode__(self):
        return self.header
