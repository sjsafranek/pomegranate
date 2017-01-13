#!/usr/bin/python

from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator

class Furniture(models.Model):
    TYPES = (
        ('TABLE', 'TABLE'),
        ('CHAIR', 'CHAIR'),
        ('COUCH', 'COUCH'),
        ('DESK', 'DESK'),
    )
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    furinture_type = models.CharField(max_length=5, choices=TYPES)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=25)
    latitude = models.FloatField(validators = [MinValueValidator(-90), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators = [MinValueValidator(-180.0), MaxValueValidator(180.0)])
    # owner = models.ForeignKey(Group)

class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=25)
    state = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(1)])
    noise = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    users = models.IntegerField()
    outlets = models.IntegerField()
    collab = models.IntegerField()
    laptops = models.IntegerField()
    furniture_moved = models.IntegerField()

