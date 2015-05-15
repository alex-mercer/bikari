# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacka', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(default=None, to='hacka.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'P', b'Pending'), (b'A', b'Accepted'), (b'R', b'Rejected'), (b'C', b'Canceled')]),
        ),
    ]
