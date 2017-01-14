#!/usr/bin/python

from django.db import models
#from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator

from . import utils

'''
class UnixDateTimeField(models.DateTimeField):

    __metaclass__ = models.SubfieldBase

    def get_internal_type(self):
        return 'PositiveIntegerField'

    def to_python(self, value):
        if value is None or isinstance(value, datetime):
            return value
        if isinstance(value, date):
            return datetime(value.year, value.month, value.day)
        return datetime.fromtimestamp( float(value) )

    def get_db_prep_value(self, value):
        return int( time.mktime( value.timetuple() ) )

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.to_python(value).strftime('%Y-%m-%d %H:%M:%S')
'''


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
    floor = models.IntegerField(validators = [MinValueValidator(-5), MaxValueValidator(5)])
    furinture_type = models.CharField(max_length=5, choices=TYPES)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=25)
    latitude = models.FloatField(validators = [MinValueValidator(-90), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators = [MinValueValidator(-180.0), MaxValueValidator(180.0)])
    #unix_timestamp = UnixDateTimeField()
    unix_timestamp = models.IntegerField(default=utils.unix_timestamp())

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
    #unix_timestamp = UnixDateTimeField()
    unix_timestamp = models.IntegerField(default=utils.unix_timestamp())


#from django.contrib.gis.geos import Point
#pnt = Point(12.4604, 43.9420)
#geom = models.PointField(srid=4326)
#from django.contrib.gis import admin
#from .models import WorldBorder
#admin.site.register(WorldBorder, admin.GeoModelAdmin)

#from django.contrib.gis import admin
#url(r'^admin/', admin.site.urls),
