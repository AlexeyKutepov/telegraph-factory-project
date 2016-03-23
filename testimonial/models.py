from django.db import models

# Create your models here.

from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Testimonial(CMSPlugin):
    text = models.TextField()
    user_name = models.CharField(max_length=100)
    user_position = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

    def __unicode__(self):
        return self.user_name

