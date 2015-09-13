# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20150912_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
