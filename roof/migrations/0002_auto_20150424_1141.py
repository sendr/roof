# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='short_desc',
            field=models.CharField(default=b'This will be short description', max_length=200, verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xbe\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articles',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 41, 5, 207420, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
