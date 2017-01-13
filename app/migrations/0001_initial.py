# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-13 21:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=25)),
                ('floor', models.IntegerField(validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(5)])),
                ('furinture_type', models.CharField(choices=[('TABLE', 'TABLE'), ('CHAIR', 'CHAIR'), ('COUCH', 'COUCH'), ('DESK', 'DESK')], max_length=5)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(max_length=25)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90.0)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('unix_timestamp', models.IntegerField(default=1484344216)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=25)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=25)),
                ('state', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('noise', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('users', models.IntegerField()),
                ('outlets', models.IntegerField()),
                ('collab', models.IntegerField()),
                ('laptops', models.IntegerField()),
                ('furniture_moved', models.IntegerField()),
                ('unix_timestamp', models.IntegerField(default=1484344216)),
            ],
        ),
    ]
