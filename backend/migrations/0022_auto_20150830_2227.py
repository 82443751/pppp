# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_auto_20150814_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='items',
        ),
        migrations.AddField(
            model_name='questions',
            name='items',
            field=models.ManyToManyField(to='backend.Items', blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='is_conflict_style_test',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u51b2\u7a81\u98ce\u683c\u6d4b\u8bd5\uff1f'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='is_result_from_class',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u4ee5\u95ee\u9898\u5206\u7c7b\u4f5c\u7ed3\u679c\uff1f'),
        ),
    ]
