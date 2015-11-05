# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0002_auto_20150814_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Task', models.CharField(max_length=200)),
                ('objective', models.CharField(max_length=200)),
                ('Due_Date', models.DateTimeField()),
                ('Finish_Date', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
