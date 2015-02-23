# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statsanalyze', '0007_auto_20150127_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='NowEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField()),
                ('ocreddirectly', models.BooleanField()),
                ('idnumber', models.CharField(max_length=50)),
                ('entry_date', models.DateTimeField(verbose_name=b'Entry datetime')),
                ('added_time', models.DateTimeField(default=datetime.datetime(2015, 2, 23, 16, 24, 19, 723430, tzinfo=utc))),
                ('ap', models.PositiveIntegerField()),
                ('bronze', models.PositiveIntegerField()),
                ('silver', models.PositiveIntegerField()),
                ('gold', models.PositiveIntegerField()),
                ('platinum', models.PositiveIntegerField()),
                ('onyx', models.PositiveIntegerField()),
                ('nomedal', models.PositiveIntegerField()),
                ('linksactiv', models.PositiveIntegerField()),
                ('fieldsactiv', models.PositiveIntegerField()),
                ('pwned', models.PositiveIntegerField()),
                ('mucontrol', models.PositiveIntegerField()),
                ('agentdb', models.ForeignKey(to='statsanalyze.Agent')),
                ('creator', models.ForeignKey(related_name='nowentrycreator', to='statsanalyze.User')),
                ('owner', models.ForeignKey(related_name='nowentryowner', to='statsanalyze.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entry',
            name='glyph',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='uniqmis',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 23, 16, 24, 19, 721158, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
