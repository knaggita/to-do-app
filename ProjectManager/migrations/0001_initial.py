# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('tasks', models.CharField(max_length=200)),
                ('responsibility', models.CharField(max_length=200)),
                ('objective', models.CharField(max_length=200)),
                ('Date_Due', models.DateTimeField(verbose_name=b'date published')),
                ('Date_Finished', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ContactsName', models.CharField(max_length=200)),
                ('About', models.CharField(max_length=200)),
                ('WayForward', models.IntegerField()),
                ('DateSeen', models.DateTimeField(verbose_name=b'date published')),
                ('nextMtg', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Task', models.CharField(max_length=200)),
                ('objective', models.CharField(max_length=200)),
                ('Due_Date', models.DateTimeField()),
                ('Finish_Date', models.DateTimeField()),
            ],
        ),
    ]
