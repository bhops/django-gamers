# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20150913_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='url',
            new_name='gr_url',
        ),
    ]
