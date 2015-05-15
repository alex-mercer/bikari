from django.contrib import admin
from hacka import models


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status')
    actions = ['accept_registrations','reject_registrations']

    def accept_registrations(self, request, queryset):
        for registeration in queryset:
            registeration.status = 'A'
            registeration.save()

    def reject_registrations(self, request, queryset):
        for registeration in queryset:
            registeration.status = 'R'
            registeration.save()


admin.site.register(models.HackaUser)
admin.site.register(models.Tag)
admin.site.register(models.Event)
admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.City)
