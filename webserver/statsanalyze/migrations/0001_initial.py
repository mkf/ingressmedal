# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codename', models.CharField(max_length=50)),
                ('public', models.BooleanField()),
                ('knownemailone', models.EmailField(max_length=75)),
                ('knownemailtwo', models.EmailField(max_length=75)),
                ('knownemailthree', models.EmailField(max_length=75)),
                ('googleplusurlone', models.URLField()),
                ('googleplusurltwo', models.URLField()),
                ('googleplusurlthree', models.URLField()),
                ('otherurlone', models.URLField()),
                ('otherurltwo', models.URLField()),
                ('otherurlthree', models.URLField()),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField()),
                ('ocreddirectly', models.BooleanField()),
                ('idnumber', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=50)),
                ('entry_date', models.DateTimeField(verbose_name=b'Entry datetime')),
                ('added_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('ap', models.PositiveIntegerField()),
                ('bronze', models.PositiveIntegerField()),
                ('silver', models.PositiveIntegerField()),
                ('gold', models.PositiveIntegerField()),
                ('platinum', models.PositiveIntegerField()),
                ('onyx', models.PositiveIntegerField()),
                ('nomedal', models.PositiveIntegerField()),
                ('uniqvis', models.PositiveIntegerField()),
                ('seer', models.PositiveIntegerField()),
                ('xm', models.PositiveIntegerField()),
                ('walk', models.PositiveIntegerField()),
                ('depl', models.PositiveIntegerField()),
                ('link', models.PositiveIntegerField()),
                ('field', models.PositiveIntegerField()),
                ('allfieldmusum', models.PositiveIntegerField()),
                ('longestlink', models.PositiveIntegerField()),
                ('largestfield', models.PositiveIntegerField()),
                ('rech', models.PositiveIntegerField()),
                ('capt', models.PositiveIntegerField()),
                ('uniqcapt', models.PositiveIntegerField()),
                ('mods', models.PositiveIntegerField()),
                ('destr', models.PositiveIntegerField()),
                ('neutr', models.PositiveIntegerField()),
                ('destrlink', models.PositiveIntegerField()),
                ('destrfield', models.PositiveIntegerField()),
                ('guard', models.PositiveIntegerField()),
                ('guardnow', models.PositiveIntegerField()),
                ('guardlink', models.PositiveIntegerField()),
                ('maxlinklenxdays', models.PositiveIntegerField()),
                ('guardfield', models.PositiveIntegerField()),
                ('maxfieldmuxdays', models.PositiveIntegerField()),
                ('hack', models.PositiveIntegerField()),
                ('edits', models.PositiveIntegerField()),
                ('photos', models.PositiveIntegerField()),
                ('agentdb', models.ForeignKey(to='statsanalyze.Agent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personality', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entry',
            name='creator',
            field=models.ForeignKey(related_name='entrycreator', to='statsanalyze.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='owner',
            field=models.ForeignKey(related_name='entryowner', to='statsanalyze.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agent',
            name='creator',
            field=models.ForeignKey(related_name='agentcreator', to='statsanalyze.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agent',
            name='dbowner',
            field=models.ForeignKey(related_name='agentdbowner', to='statsanalyze.User'),
            preserve_default=True,
        ),
    ]
