# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20150101_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluser',
            options={'ordering': ['add_time'], 'verbose_name': 'User information', 'verbose_name_plural': 'User information'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['add_time'], 'verbose_name': 'Options for question', 'verbose_name_plural': 'Options for question'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['add_time', 'question_class'], 'verbose_name': 'Question', 'verbose_name_plural': 'Question'},
        ),
        migrations.AlterModelOptions(
            name='questionclass',
            options={'ordering': ['add_time'], 'verbose_name': 'Question Class', 'verbose_name_plural': 'Question Class'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['add_time'], 'verbose_name': 'Single test', 'verbose_name_plural': 'Single test'},
        ),
        migrations.AlterModelOptions(
            name='resultexplain',
            options={'ordering': ['add_time'], 'verbose_name': 'Description for this score', 'verbose_name_plural': 'Description for this score'},
        ),
        migrations.AlterModelOptions(
            name='useranwser',
            options={'ordering': ['add_time', 'user', 'questions'], 'verbose_name': 'User choice', 'verbose_name_plural': 'User choice'},
        ),
        migrations.AlterModelOptions(
            name='userresult',
            options={'ordering': ['add_time', 'user', 'is_pay'], 'verbose_name': 'User score', 'verbose_name_plural': 'User score'},
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='age',
            field=models.CharField(max_length=4, verbose_name='Age'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='Email address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Mobile phone number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='sex',
            field=models.CharField(db_index=True, max_length=1, verbose_name='Sex', choices=[(b'1', 'Male'), (b'0', 'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='en_content',
            field=models.CharField(help_text='Example: Lower', max_length=300, verbose_name='English'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='score',
            field=models.IntegerField(default=1, help_text='Weight for this option', verbose_name='Weight'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='zh_content',
            field=models.CharField(help_text='Sample: Mild', max_length=300, verbose_name='Chinese'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='zh_content',
            field=models.CharField(max_length=500, verbose_name='Chinese', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionclass',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionclass',
            name='zh_content',
            field=models.CharField(max_length=300, verbose_name='Chinese'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='en_content',
            field=models.CharField(max_length=500, null=True, verbose_name='Description [English]', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='en_title',
            field=models.CharField(max_length=300, verbose_name='Title [English]', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='is_need_pay',
            field=models.BooleanField(default=False, db_index=True, verbose_name='Need payment or not'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='price',
            field=models.FloatField(default=0, verbose_name='Price'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='zh_content',
            field=models.CharField(max_length=500, null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='zh_title',
            field=models.CharField(max_length=300, verbose_name='Title', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='en_content',
            field=ckeditor.fields.RichTextField(verbose_name='Detailed descripiton [English]'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='en_simple_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Simple descripiton [English]', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='max_score',
            field=models.IntegerField(help_text='Including', verbose_name='Upper value of this score range'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='min_score',
            field=models.IntegerField(help_text='Including', verbose_name='Lower value of this score range'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_content',
            field=ckeditor.fields.RichTextField(verbose_name='Detailed description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='zh_simple_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Simple descripiton', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useranwser',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='is_pay',
            field=models.BooleanField(default=False, db_index=True, verbose_name='Has been paid or not'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='pay_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Payment time', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='price',
            field=models.FloatField(default=0, verbose_name='Price'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='trade_no',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='Alipay order no.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userscoreexplain',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userscoreexplain',
            name='score',
            field=models.IntegerField(default=-1, verbose_name='Weight', blank=True),
            preserve_default=True,
        ),
    ]
