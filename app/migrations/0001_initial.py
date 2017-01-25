# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-25 04:32
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
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
                ('rfid', models.CharField(max_length=50)),
                ('furniture_type', models.CharField(choices=[('COUCH', 'COUCH'), ('CHAIR ARM', 'CHAIR ARM'), ('CHAIR TALL', 'CHAIR TALL'), ('CHAIR YELLOW', 'CHAIR YELLOW'), ('CHAIR GREY', 'CHAIR GREY'), ('CHAIR ARMLESS', 'CHAIR ARMLESS'), ('TABLE TALL', 'TABLE TALL'), ('TABLE SHORT', 'TABLE SHORT'), ('TABLE REGULAR', 'TABLE REGULAR'), ('TABLE GLASS', 'TABLE GLASS'), ('DESK PUBLIC', 'DESK PUBLIC'), ('DESK CONSULTATION', 'DESK CONSULTATION'), ('DESK TALL', 'DESK TALL'), ('DESK OSX', 'DESK OSX'), ('DESK WIN', 'DESK WIN'), ('DESK OSX w/ SCANNER', 'DESK OSX w/ SCANNER'), ('DESK WIN w/ SCANNER', 'DESK WIN w/ SCANNER'), ('DESK LAPTOP', 'DESK LAPTOP'), ('TABLE BIG MAP', 'TABLE BIG MAP')], max_length=25)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('unix_timestamp', models.IntegerField()),
                ('created_by', models.CharField(max_length=25)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90.0)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person_type', models.CharField(choices=[('ACADEMIC', 'ACADEMIC'), ('PUBLIC', 'PUBLIC')], max_length=25)),
                ('collab', models.BooleanField()),
                ('computer_type', models.CharField(choices=[('DESKTOP', 'DESKTOP'), ('LAPTOP', 'LAPTOP'), ('NONE', 'NONE')], max_length=25)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('unix_timestamp', models.IntegerField()),
                ('created_by', models.CharField(max_length=25)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90.0)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('unix_timestamp', models.IntegerField()),
                ('created_by', models.CharField(max_length=25)),
                ('messy', models.BooleanField()),
                ('noise', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=50)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('unix_timestamp', models.IntegerField()),
                ('created_by', models.CharField(max_length=25)),
                ('outlets_used', models.IntegerField()),
            ],
        ),
    ]
