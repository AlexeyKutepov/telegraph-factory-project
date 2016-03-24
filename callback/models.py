from django.db import models

# Create your models here.
from django.utils import timezone


class Callback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.name:
            return self.name
        elif self.email:
            return self.email
        elif self.phone:
            return self.phone

    def __unicode__(self):
        if self.name:
            return self.name
        elif self.email:
            return self.email
        elif self.phone:
            return self.phone


class Order(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        elif self.email:
            return self.email
        elif self.phone:
            return self.phone

    def __unicode__(self):
        if self.name:
            return self.name
        elif self.email:
            return self.email
        elif self.phone:
            return self.phone


class Question(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    question = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        elif self.email:
            return self.email
        elif self.phone:
            return self.phone

    def __unicode__(self):
        if self.name:
            return self.name
        elif self.email:
            return self.email
        elif self.phone:
            return self.phone