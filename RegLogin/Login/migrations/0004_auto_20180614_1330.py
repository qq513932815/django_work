# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-06-14 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20180614_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='last_login_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='register_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]