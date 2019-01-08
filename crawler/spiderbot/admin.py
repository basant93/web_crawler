from django.contrib import admin

# Register your models here.

from spiderbot.models import WebImage, WebPage

admin.site.register(WebImage)
admin.site.register(WebPage)