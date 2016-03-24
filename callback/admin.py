from django.contrib import admin

# Register your models here.
from callback.models import Callback, Question, Order


@admin.register(Callback)
class Callback(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'datetime', )
    list_filter = ('name', 'email', 'phone', )


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'datetime', 'question', )
    list_filter = ('name', 'email', 'phone', 'question', )


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'datetime', 'description', )
    list_filter = ('name', 'email', 'phone', 'description', )