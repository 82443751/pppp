# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_auto_20150814_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_single',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u5355\u9009'),
        ),
        migrations.AddField(
            model_name='questions',
            name='is_conflict_style_test',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u51b2\u7a81\u98ce\u683c\u6d4b\u8bd5'),
        ),
        migrations.AlterField(
            model_name='question',
            name='items',
            field=models.ManyToManyField(to='backend.Items', blank=True),
        ),
    ]
