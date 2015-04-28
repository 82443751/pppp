# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20150326_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='max_score',
            field=models.CharField(default='', help_text='\u5305\u542b\uff0c\u82e5\u6307\u5b9a\u6b64\u503c\uff0c\u5219\u7ed3\u679c\u5206\u6570\u9ad8\u4e8e\u6b64\u503c\u65f6\u4f1a\u8f6c\u5230\u4e00\u4e2a\u63d0\u793a\uff0c\u8868\u793a\u7ed3\u679c\u65e0\u6548', max_length=2, verbose_name='\u65e0\u6548\u533a\u95f4\u9ad8\u503c'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questions',
            name='min_score',
            field=models.CharField(default='', help_text='\u5305\u542b\uff0c\u82e5\u6307\u5b9a\u6b64\u503c\uff0c\u5219\u7ed3\u679c\u5206\u6570\u5c0f\u4e8e\u6b64\u503c\u65f6\u4f1a\u8f6c\u5230\u4e00\u4e2a\u63d0\u793a\uff0c\u8868\u793a\u7ed3\u679c\u65e0\u6548', max_length=2, verbose_name='\u65e0\u6548\u533a\u95f4\u4f4e\u503c'),
            preserve_default=True,
        ),
    ]
