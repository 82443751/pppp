# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_auto_20150714_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultexplain',
            name='is_show_content',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5728\u8be6\u7ec6\u7ed3\u679c\u4e2d\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='resultexplain',
            name='is_show_detail',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5728\u7406\u8be6\u7ec6\u7ed3\u679c\u4e2d\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='resultexplain',
            name='is_show_simple_content',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5728\u7b80\u8981\u7ed3\u679c\u4e2d\u663e\u793a'),
        ),
    ]
