# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tagging.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=tagging.fields.TagField(max_length=255, verbose_name=b'Tags', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 15, 21, 41, 468049, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
