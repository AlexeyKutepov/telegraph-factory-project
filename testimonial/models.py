from django.db import models

# Create your models here.

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

from django.db import models


class Testimonial(CMSPlugin):
    photo = FilerImageField(blank=True, null=True)
    text = models.TextField()
    user_name = models.CharField(max_length=100)
    user_position = models.CharField(max_length=100)
    site = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user_name

    def __unicode__(self):
        return self.user_name

