# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='default_id',
            field=models.IntegerField(default=0),
        ),
    ]
