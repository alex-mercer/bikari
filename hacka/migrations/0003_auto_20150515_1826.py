# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacka', '0002_auto_20150515_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='background',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
