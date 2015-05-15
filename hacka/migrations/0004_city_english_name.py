# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hacka', '0003_auto_20150515_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='english_name',
            field=models.CharField(default=datetime.datetime(2015, 5, 15, 14, 10, 46, 282376, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
