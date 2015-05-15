# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from geoposition.fields import GeopositionField
from django_jalali.db import models as jmodels


class HackaUser(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=40)


class City(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
    admins = models.ManyToManyField(User, limit_choices_to={'user__is_staff': True})


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start = jmodels.jDateTimeField()
    end = jmodels.jDateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)
    position = GeopositionField()
    city = models.ForeignKey(City)

    def get_absolute_url(self):
        return reverse('show_event', args=[self.city.name, self.id])


class Registration(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
        ('C', 'Canceled'),
    )
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        super(Registration, self).save(*args, **kwargs)
        if self.pk is None:
            return
        orig = Registration.objects.get(pk=self.pk)
        if orig.status != self.status:
            event = '<a href="%s">%s</a>' % (self.event.get_absolute_url(), self.event.title)
            message = ''
            if self.status == 'A':
                message = u'تبریک ثبت‌نام شما برای رویداد %s تایید شد! منتظرتان هستیم' % event
            elif self.status == 'R':
                message = u'تسلیت! ثبت‌نام شما برای رویداد %s رد شد. امیدواریم در رویداد‌های بعدی شاهد حضور شما باشیم.' % event
            if message:
                self.user.email_user(u'نتیجه ثبت‌نام شما در رویداد %s' % self.event.title, '', html_message=message)

