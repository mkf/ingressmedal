# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statsanalyze', '0002_auto_20150126_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='guardnow',
        ),
        migrations.AddField(
            model_name='entry',
            name='recruiter',
            field=models.PositiveIntegerField(default=None, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='timepart',
            field=models.CharField(default=b'AllTime', max_length=7, choices=[(b'AllTime', b'AllTime'), (b'Month', b'Month'), (b'Week', b'Week')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 13, 3, 46, 866443, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
