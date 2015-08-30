# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchups', '0003_schedule_scheduleblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleblock',
            name='schedule',
            field=models.ForeignKey(to='matchups.Schedule', related_name='blocks'),
        ),
    ]
