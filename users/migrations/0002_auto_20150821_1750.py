# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ('user',)},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('?', 'Prefer not to disclose')], max_length=1, default='M'),
        ),
    ]
