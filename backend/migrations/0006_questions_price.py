# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_userscoreexplain_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='price',
            field=models.FloatField(default=0, verbose_name='\u4ef7\u683c'),
            preserve_default=True,
        ),
    ]
