# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20150912_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='released',
            field=models.DateField(null=True),
        ),
    ]
