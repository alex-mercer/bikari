# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from geoposition.fields import GeopositionField
from django_jalali.db import models as jmodels


class HackaUser(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(blank=True)

    def __unicode__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    english_name = models.CharField(max_length=100, unique=True)
    position = GeopositionField()
    admins = models.ManyToManyField(User)
    picture = models.ImageField(blank=True)
    background = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('show_city', args=[self.english_name])

    def __unicode__(self):
        return self.name



class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start = jmodels.jDateTimeField()
    end = jmodels.jDateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)
    position = GeopositionField()
    city = models.ForeignKey(City)
    picture = models.ImageField(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        path = reverse('show_event', args=[self.city.english_name, self.id])
        return "http://localhost:8000%s" % path


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
        if self.pk is not None:
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
        super(Registration, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username + " vs. " + self.event.title

