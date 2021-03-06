# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usertest', '0002_userinfo_default_id'),
        ('goodstest', '0003_auto_20181019_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('cgoods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodstest.GoodsInfo')),
                ('cuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usertest.UserInfo')),
            ],
        ),
    ]
