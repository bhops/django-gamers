# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import matchups.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matchups', '0002_auto_20150825_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleBlock',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday')], max_length=2, default='M')),
                ('time_from', models.TimeField(default='00:00')),
                ('time_to', models.TimeField(default='23:59')),
                ('schedule', models.ForeignKey(to='matchups.Schedule')),
            ],
        ),
    ]
