# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_auto_20151010_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['order'], 'verbose_name': '\u95ee\u9898\u53ef\u9009\u9879', 'verbose_name_plural': '\u95ee\u9898\u53ef\u9009\u9879'},
        ),
        migrations.AddField(
            model_name='option',
            name='order',
            field=models.IntegerField(default=1, help_text='\u6570\u503c\u8d8a\u5c0f\u663e\u793a\u4f4d\u7f6e\u8d8a\u9760\u524d', verbose_name='\u663e\u793a\u987a\u5e8f'),
        ),
    ]
