# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20150101_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='explain',
            field=models.ManyToManyField(to='backend.ResultExplain', verbose_name='\u5206\u503c\u8bf4\u660e'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.ManyToManyField(to='backend.Question', verbose_name='\u95ee\u9898'),
            preserve_default=True,
        ),
    ]
