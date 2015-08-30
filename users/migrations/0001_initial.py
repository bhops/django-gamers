# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('?', 'Prefer not to disclose')], default='M')),
                ('about', models.CharField(max_length=255, default="This user hasn't updated their profile.")),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
    ]
