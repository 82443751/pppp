# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20141229_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultexplain',
            name='en_content',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='en_simple_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Simple Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_content',
            field=ckeditor.fields.RichTextField(verbose_name='\u8be6\u7ec6\u8bf4\u660e'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_simple_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u7b80\u8981\u8bf4\u660e', blank=True),
            preserve_default=True,
        ),
    ]
