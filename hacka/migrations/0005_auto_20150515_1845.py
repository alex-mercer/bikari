# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacka', '0004_city_english_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='english_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
