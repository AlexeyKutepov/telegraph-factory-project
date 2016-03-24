from django.contrib import admin

# Register your models here.
from subscribe.models import Subscriber


@admin.register(Subscriber)
class Subscriber(admin.ModelAdmin):
    list_display = ('email', )
    list_filter = ('email', )
