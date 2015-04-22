# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20141219_0031'),
    ]

    operations = [
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
            field=models.ManyToManyField(to='backend.ResultExplain', through='backend.UserScoreExplain'),
            preserve_default=True,
        ),
    ]
