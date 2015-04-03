# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_questions_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='price',
            field=models.FloatField(default=0, verbose_name='\u4ef7\u683c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userscoreexplain',
            name='score',
            field=models.IntegerField(default=-1, verbose_name='\u5206\u503c', blank=True),
            preserve_default=True,
        ),
    ]
