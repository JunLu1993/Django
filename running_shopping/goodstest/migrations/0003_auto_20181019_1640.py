# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 08:40
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('goodstest', '0002_auto_20181018_1547'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='categoryinfo',
            managers=[
                ('category', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='goodsinfo',
            managers=[
                ('goods', django.db.models.manager.Manager()),
            ],
        ),
    ]
