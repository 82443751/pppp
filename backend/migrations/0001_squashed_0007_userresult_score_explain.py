# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'backend', '0001_initial'), (b'backend', '0002_auto_20141112_1446'), (b'backend', '0003_auto_20141121_0744'), (b'backend', '0004_auto_20141219_0031'), (b'backend', '0005_auto_20141220_0538'), (b'backend', '0006_remove_userresult_score_explain'), (b'backend', '0007_userresult_score_explain')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zh_content', models.CharField(help_text='\u793a\u4f8b\uff1a\u8f7b\u5fae', max_length=300, verbose_name='\u4e2d\u6587\u7b54\u6848')),
                ('en_content', models.CharField(help_text='Example: Lower', max_length=300, verbose_name='English Answer')),
                ('score', models.IntegerField(default=1, help_text='\u8be5\u9009\u9879\u7684\u5206\u503c', verbose_name='\u5206\u503c')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'ordering': ['add_time'],
                'verbose_name': '\u95ee\u9898\u53ef\u9009\u9879',
                'verbose_name_plural': '\u95ee\u9898\u53ef\u9009\u9879',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zh_content', models.CharField(max_length=500, verbose_name='\u4e2d\u6587', db_index=True)),
                ('en_content', models.CharField(max_length=500, verbose_name='English', db_index=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
                ('options', models.ManyToManyField(to=b'backend.Option')),
            ],
            options={
                'ordering': ['add_time', 'question_class'],
                'verbose_name': '\u95ee\u9898',
                'verbose_name_plural': '\u95ee\u9898',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zh_content', models.CharField(max_length=300, verbose_name='\u4e2d\u6587')),
                ('en_content', models.CharField(max_length=300, verbose_name='English')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'ordering': ['add_time'],
                'verbose_name': '\u95ee\u9898\u7c7b\u522b',
                'verbose_name_plural': '\u95ee\u9898\u7c7b\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zh_title', models.CharField(max_length=300, verbose_name='\u6807\u9898', db_index=True)),
                ('en_title', models.CharField(max_length=300, verbose_name='Title', db_index=True)),
                ('zh_content', models.CharField(max_length=500, null=True, verbose_name='\u8bf4\u660e', blank=True)),
                ('en_content', models.CharField(max_length=500, null=True, verbose_name='Description', blank=True)),
                ('is_need_pay', models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u9700\u8981\u4ed8\u8d39')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'ordering': ['add_time'],
                'verbose_name': '\u5355\u5957\u6d4b\u8bd5',
                'verbose_name_plural': '\u5355\u5957\u6d4b\u8bd5',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultExplain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_score', models.IntegerField(help_text='\u5305\u542b', verbose_name='\u5206\u503c\u533a\u95f4\u4f4e\u503c')),
                ('max_score', models.IntegerField(help_text='\u5305\u542b', verbose_name='\u5206\u503c\u533a\u95f4\u9ad8\u503c')),
                ('zh_simple_content', models.TextField(null=True, verbose_name='\u7b80\u8981\u8bf4\u660e', blank=True)),
                ('en_simple_content', models.TextField(null=True, verbose_name='Simple Description', blank=True)),
                ('zh_content', models.TextField(verbose_name='\u8be6\u7ec6\u8bf4\u660e')),
                ('en_content', models.TextField(verbose_name='Description')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'ordering': ['add_time'],
                'verbose_name': '\u5206\u6570\u8bf4\u660e',
                'verbose_name_plural': '\u5206\u6570\u8bf4\u660e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EvalUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d', db_index=True)),
                ('sex', models.CharField(db_index=True, max_length=1, verbose_name='\u6027\u522b', choices=[(b'1', '\u7537'), (b'0', '\u5973')])),
                ('age', models.CharField(max_length=4, verbose_name='\u5e74\u9f84')),
                ('email', models.EmailField(max_length=75, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=20, verbose_name='\u624b\u673a')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'ordering': ['add_time'],
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAnwser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
                ('option', models.ForeignKey(to='backend.Option')),
                ('question', models.ForeignKey(to='backend.Question')),
                ('questions', models.ForeignKey(to='backend.Questions')),
                ('user', models.ForeignKey(to='backend.EvalUser')),
            ],
            options={
                'ordering': ['add_time', 'user', 'questions'],
                'verbose_name': '\u7528\u6237\u9009\u62e9',
                'verbose_name_plural': '\u7528\u6237\u9009\u62e9',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_pay', models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u652f\u4ed8')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
                ('explain', models.ManyToManyField(to=b'backend.ResultExplain')),
                ('questions', models.ForeignKey(to='backend.Questions')),
                ('user', models.ForeignKey(to='backend.EvalUser')),
            ],
            options={
                'ordering': ['add_time', 'user', 'is_pay'],
                'verbose_name': '\u7528\u6237\u5f97\u5206',
                'verbose_name_plural': '\u7528\u6237\u5f97\u5206',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='questions',
            name='explain',
            field=models.ManyToManyField(to=b'backend.ResultExplain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questions',
            name='question',
            field=models.ManyToManyField(to=b'backend.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='question_class',
            field=models.ForeignKey(blank=True, to='backend.QuestionClass', null=True),
            preserve_default=True,
        ),

        migrations.AddField(
            model_name='resultexplain',
            name='question_class',
            field=models.ForeignKey(blank=True, to='backend.QuestionClass', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultexplain',
            name='user_score',
            field=models.IntegerField(db_index=True, null=True, verbose_name='\u7528\u6237\u5f97\u5206', blank=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='UserScoreExplain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name='\u5206\u503c')),
                ('explain', models.ForeignKey(to='backend.ResultExplain')),
                ('user_result', models.ForeignKey(to='backend.UserResult')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userresult',
            name='explain',
        ),
        migrations.AddField(
            model_name='userresult',
            name='score_explain',
            field=models.ManyToManyField(to=b'backend.ResultExplain', through='backend.UserScoreExplain'),
            preserve_default=True,
        ),
    ]
