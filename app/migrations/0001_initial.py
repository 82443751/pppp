# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20141112_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='One',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test', models.ForeignKey(to='backend.Option')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
