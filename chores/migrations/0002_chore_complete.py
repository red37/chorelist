# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='complete',
            field=models.BooleanField(default=True),
        ),
    ]
