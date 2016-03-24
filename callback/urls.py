__author__ = 'Alexey Kutepov'

from django.conf.urls import patterns, url
from callback import views

urlpatterns = patterns('',
        url(r'^callback/$', views.callback, name='callback'),
        url(r'^question/$', views.question, name='question'),
        url(r'^order/$', views.order, name='order'),
)

