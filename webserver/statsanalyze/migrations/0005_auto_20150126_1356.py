# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statsanalyze', '0004_auto_20150126_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 13, 56, 7, 695602, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
