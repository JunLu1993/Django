# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodstest', '0005_auto_20181026_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentinfo',
            name='grade',
            field=models.IntegerField(default=5),
        ),
    ]
