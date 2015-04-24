# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u0410\u0434\u0440\u0435\u0441',
                'verbose_name_plural': '\u0410\u0434\u0440\u0435\u0441\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.CharField(unique=True, max_length=30)),
                ('image', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 40, 50, 274578, tzinfo=utc))),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=True, verbose_name=b'Is public')),
                ('tags', tagging.fields.TagField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u0438',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=50)),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.EmailField(max_length=30)),
            ],
            options={
                'verbose_name': '\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430',
                'verbose_name_plural': '\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430',
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
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0430\u043b\u0435\u0440\u0435\u044f',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0430\u043b\u0435\u0440\u0435\u044f',
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
                'verbose_name': '\u041e \u043d\u0430\u0441',
                'verbose_name_plural': '\u041e \u043d\u0430\u0441',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d',
                'verbose_name_plural': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b',
            },
            bases=(models.Model,),
        ),
    ]
