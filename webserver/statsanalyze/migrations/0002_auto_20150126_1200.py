# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statsanalyze', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='codename',
        ),
        migrations.AlterField(
            model_name='agent',
            name='googleplusurlone',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='googleplusurlthree',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='googleplusurltwo',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='knownemailone',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='knownemailthree',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='knownemailtwo',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='otherurlone',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='otherurlthree',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agent',
            name='otherurltwo',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 12, 0, 58, 590723, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='edits',
            field=models.PositiveIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='guardnow',
            field=models.PositiveIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='photos',
            field=models.PositiveIntegerField(blank=True),
            preserve_default=True,
        ),
    ]
