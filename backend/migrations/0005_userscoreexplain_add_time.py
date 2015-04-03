# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20141225_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscoreexplain',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added time', null=True),
            preserve_default=True,
        ),
    ]
