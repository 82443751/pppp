# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20150120_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='detail_price',
            field=models.FloatField(default=0, verbose_name='\u8be6\u7ec6\u62a5\u544a\u4ef7\u683c'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultexplain',
            name='en_detail',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u66f4\u8be6\u7ec6\u8bf4\u660e[\u82f1\u6587]', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultexplain',
            name='zh_detail',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u66f4\u8be6\u7ec6\u8bf4\u660e', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userresult',
            name='detail_our_trade_no',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name='\u8be6\u7ec6\u62a5\u544a\u8ba2\u5355\u53f7', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userresult',
            name='detail_pay_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u8be6\u7ec6\u62a5\u544a\u652f\u4ed8\u65f6\u95f4', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userresult',
            name='detail_price',
            field=models.FloatField(default=0, verbose_name='Price'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userresult',
            name='detail_trade_no',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u8be6\u7ec6\u62a5\u544a\u652f\u4ed8\u5b9d\u8ba2\u5355\u53f7', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userresult',
            name='is_pay_detail',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u652f\u4ed8\u8be6\u7ec6\u62a5\u544a'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='en_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Detailed descripiton [English]', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Detailed description', blank=True),
            preserve_default=True,
        ),
    ]
