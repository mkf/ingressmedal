# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statsanalyze', '0005_auto_20150126_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='owncodename',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 27, 9, 22, 23, 605831, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
