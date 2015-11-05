# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='ContactsName',
            new_name='ContactName',
        ),
        migrations.AlterField(
            model_name='actionplan',
            name='Date_Due',
            field=models.DateTimeField(verbose_name=b'due date'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='DateSeen',
            field=models.DateTimeField(verbose_name=b'date seen'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='WayForward',
            field=models.CharField(max_length=200),
        ),
    ]
