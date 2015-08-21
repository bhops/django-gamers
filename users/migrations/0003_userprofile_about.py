# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150821_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.CharField(default='', max_length=255),
        ),
    ]
