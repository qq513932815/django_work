# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-06-14 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20180614_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='is_ban',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='login',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='role',
            field=models.CharField(default=1, max_length=1),
        ),
    ]
