# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookingforpost',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lookingforpost',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='lookingforpost',
            name='filled',
            field=models.BooleanField(default=False),
        ),
    ]
