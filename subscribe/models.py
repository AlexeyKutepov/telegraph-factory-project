from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email
