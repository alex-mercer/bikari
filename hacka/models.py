from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField
from django_jalali.db import models as jmodels


class HackaUser(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=40)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start = jmodels.jDateTimeField()
    end = jmodels.jDateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)
    position = GeopositionField()


class Registration(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    )
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


class City(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
    admins = models.ManyToManyField(User, limit_choices_to={'user__is_staff': True})
