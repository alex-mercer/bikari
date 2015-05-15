from django.contrib import admin
from hacka import models

admin.site.register(models.HackaUser)
admin.site.register(models.Tag)
admin.site.register(models.Event)
admin.site.register(models.Registration)
admin.site.register(models.City)
