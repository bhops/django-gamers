# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150906_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(default='?', max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('?', 'Prefer not to disclose')]),
        ),
    ]
