# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statsanalyze', '0006_auto_20150127_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 27, 9, 57, 46, 678785, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 27, 9, 57, 59, 519699, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agent',
            name='codename',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 27, 9, 57, 25, 337513, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='owncodename',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
