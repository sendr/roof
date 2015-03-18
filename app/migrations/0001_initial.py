# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 3, 18, 15, 9, 18, 196023, tzinfo=utc))),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
                ('order', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u0438',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=30, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'gallery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IndexContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=30)),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
