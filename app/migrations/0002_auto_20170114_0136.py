# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-14 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='unix_timestamp',
            field=models.IntegerField(default=1484357795),
        ),
        migrations.AlterField(
            model_name='zone',
            name='unix_timestamp',
            field=models.IntegerField(default=1484357795),
        ),
    ]