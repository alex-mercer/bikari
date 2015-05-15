# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacka', '0005_auto_20150515_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
