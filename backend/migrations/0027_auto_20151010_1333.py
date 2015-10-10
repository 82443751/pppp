# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluser',
            options={'ordering': ['add_time'], 'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ['order'], 'verbose_name': '\u95ee\u9898\u884c\u53ef\u9009\u9879', 'verbose_name_plural': '\u95ee\u9898\u884c\u53ef\u9009\u9879'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['add_time'], 'verbose_name': '\u95ee\u9898\u53ef\u9009\u9879', 'verbose_name_plural': '\u95ee\u9898\u53ef\u9009\u9879'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['add_time', 'question_class'], 'verbose_name': '\u95ee\u9898', 'verbose_name_plural': '\u95ee\u9898'},
        ),
        migrations.AlterModelOptions(
            name='questionclass',
            options={'ordering': ['add_time'], 'verbose_name': '\u95ee\u9898\u7c7b\u522b', 'verbose_name_plural': '\u95ee\u9898\u7c7b\u522b'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['add_time'], 'verbose_name': '\u5355\u5957\u6d4b\u8bd5', 'verbose_name_plural': '\u5355\u5957\u6d4b\u8bd5'},
        ),
        migrations.AlterModelOptions(
            name='resultexplain',
            options={'ordering': ['add_time'], 'verbose_name': '\u5206\u6570\u8bf4\u660e', 'verbose_name_plural': '\u5206\u6570\u8bf4\u660e'},
        ),
        migrations.AlterModelOptions(
            name='useranwser',
            options={'ordering': ['add_time', 'user', 'questions'], 'verbose_name': '\u7528\u6237\u9009\u62e9', 'verbose_name_plural': '\u7528\u6237\u9009\u62e9'},
        ),
        migrations.AlterModelOptions(
            name='userresult',
            options={'ordering': ['add_time', 'user', 'is_pay'], 'verbose_name': '\u7528\u6237\u5f97\u5206', 'verbose_name_plural': '\u7528\u6237\u5f97\u5206'},
        ),
        migrations.AlterModelOptions(
            name='userscoreexplain',
            options={'ordering': ['add_time'], 'verbose_name': '\u7528\u6237\u7684\u5f97\u5206\u8bf4\u660e', 'verbose_name_plural': '\u7528\u6237\u7684\u5f97\u5206\u8bf4\u660e'},
        ),
        migrations.AddField(
            model_name='items',
            name='order',
            field=models.IntegerField(default=1, help_text='\u6570\u503c\u8d8a\u5c0f\u663e\u793a\u4f4d\u7f6e\u8d8a\u9760\u524d', verbose_name='\u663e\u793a\u987a\u5e8f'),
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='age',
            field=models.CharField(max_length=14, verbose_name='\u751f\u65e5'),
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u59d3\u540d', db_index=True),
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='sex',
            field=models.CharField(db_index=True, max_length=1, verbose_name='\u6027\u522b', choices=[(b'1', '\u7537'), (b'0', '\u5973')]),
        ),
        migrations.AlterField(
            model_name='option',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='option',
            name='en_content',
            field=models.CharField(help_text='Example: Lower', max_length=300, verbose_name='\u82f1\u6587'),
        ),
        migrations.AlterField(
            model_name='option',
            name='score',
            field=models.IntegerField(default=1, help_text='\u8be5\u9009\u9879\u7684\u5206\u503c', verbose_name='\u5206\u503c'),
        ),
        migrations.AlterField(
            model_name='option',
            name='zh_content',
            field=models.CharField(help_text='\u793a\u4f8b\uff1a\u8f7b\u5fae', max_length=300, verbose_name='\u4e2d\u6587'),
        ),
        migrations.AlterField(
            model_name='question',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='question',
            name='en_content',
            field=models.CharField(max_length=500, verbose_name='\u82f1\u6587', db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='zh_content',
            field=models.CharField(max_length=500, verbose_name='\u4e2d\u6587', db_index=True),
        ),
        migrations.AlterField(
            model_name='questionclass',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='questionclass',
            name='en_content',
            field=models.CharField(max_length=300, verbose_name='\u82f1\u6587'),
        ),
        migrations.AlterField(
            model_name='questionclass',
            name='zh_content',
            field=models.CharField(max_length=300, verbose_name='\u4e2d\u6587'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='detail_price',
            field=models.FloatField(default=0, verbose_name='\u8be6\u7ec6\u62a5\u544a\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='en_content',
            field=models.CharField(max_length=500, null=True, verbose_name='\u8bf4\u660e[\u82f1\u6587]', blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='en_title',
            field=models.CharField(max_length=300, verbose_name='\u6807\u9898[\u82f1\u6587]', db_index=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='explain',
            field=models.ManyToManyField(to='backend.ResultExplain', null=True, verbose_name='\u5206\u503c\u8bf4\u660e', blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='is_need_pay',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u9700\u8981\u4ed8\u8d39'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='max_score',
            field=models.CharField(default='', help_text='\u5305\u542b\uff0c\u82e5\u6307\u5b9a\u6b64\u503c\uff0c\u5219\u7ed3\u679c\u5206\u6570\u9ad8\u4e8e\u6b64\u503c\u65f6\u4f1a\u8f6c\u5230\u4e00\u4e2a\u63d0\u793a\uff0c\u8868\u793a\u7ed3\u679c\u65e0\u6548', max_length=2, verbose_name='\u65e0\u6548\u533a\u95f4\u9ad8\u503c', blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='min_score',
            field=models.CharField(default='', help_text='\u5305\u542b\uff0c\u82e5\u6307\u5b9a\u6b64\u503c\uff0c\u5219\u7ed3\u679c\u5206\u6570\u5c0f\u4e8e\u6b64\u503c\u65f6\u4f1a\u8f6c\u5230\u4e00\u4e2a\u63d0\u793a\uff0c\u8868\u793a\u7ed3\u679c\u65e0\u6548', max_length=2, verbose_name='\u65e0\u6548\u533a\u95f4\u4f4e\u503c', blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='price',
            field=models.FloatField(default=0, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.ManyToManyField(to='backend.Question', verbose_name='\u95ee\u9898'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='zh_content',
            field=models.CharField(max_length=500, null=True, verbose_name='\u8bf4\u660e', blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='zh_title',
            field=models.CharField(max_length=300, verbose_name='\u6807\u9898', db_index=True),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='en_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u8be6\u7ec6\u8bf4\u660e[\u82f1\u6587]', blank=True),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='en_detail',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u66f4\u8be6\u7ec6\u8bf4\u660e[\u82f1\u6587]', blank=True),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='en_simple_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u7b80\u8981\u8bf4\u660e[\u82f1\u6587]', blank=True),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='max_score',
            field=models.IntegerField(help_text='\u5305\u542b', verbose_name='\u5206\u503c\u533a\u95f4\u9ad8\u503c'),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='min_score',
            field=models.IntegerField(help_text='\u5305\u542b', verbose_name='\u5206\u503c\u533a\u95f4\u4f4e\u503c'),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u8be6\u7ec6\u8bf4\u660e', blank=True),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_detail',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u66f4\u8be6\u7ec6\u8bf4\u660e', blank=True),
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_simple_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u7b80\u8981\u8bf4\u660e', blank=True),
        ),
        migrations.AlterField(
            model_name='useranwser',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='detail_our_trade_no',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name='\u8be6\u7ec6\u62a5\u544a\u8ba2\u5355\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='detail_pay_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u8be6\u7ec6\u62a5\u544a\u652f\u4ed8\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='detail_price',
            field=models.FloatField(default=0, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='detail_trade_no',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u8be6\u7ec6\u62a5\u544a\u652f\u4ed8\u5b9d\u8ba2\u5355\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='is_pay',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u652f\u4ed8'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='is_pay_detail',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u652f\u4ed8\u8be6\u7ec6\u62a5\u544a'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='our_trade_no',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name='\u8ba2\u5355\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='pay_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u652f\u4ed8\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='price',
            field=models.FloatField(default=0, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='trade_no',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u652f\u4ed8\u5b9d\u8ba2\u5355\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='userscoreexplain',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4', null=True),
        ),
        migrations.AlterField(
            model_name='userscoreexplain',
            name='score',
            field=models.IntegerField(default=-1, verbose_name='\u5206\u503c', blank=True),
        ),
    ]
