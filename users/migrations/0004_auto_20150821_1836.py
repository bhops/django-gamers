# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(max_length=255, default="This user hasn't updated their profile."),
        ),
    ]
