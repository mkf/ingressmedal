# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statsanalyze', '0003_auto_20150126_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 13, 7, 55, 770498, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='edits',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='photos',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='recruiter',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
