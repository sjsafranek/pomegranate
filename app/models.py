#!/usr/bin/python

# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
#from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator

from . import utils


class Furniture(models.Model):
    TYPES = (
        ('COUCH', 'COUCH'),
        ('CHAIR ARM', 'CHAIR ARM'),
        ('CHAIR TALL', 'CHAIR TALL'),
        ('CHAIR YELLOW', 'CHAIR YELLOW'),
        ('CHAIR GREY', 'CHAIR GREY'),
        ('CHAIR ARMLESS', 'CHAIR ARMLESS'),
        ('TABLE TALL', 'TABLE TALL'),
        ('TABLE SHORT', 'TABLE SHORT'),
        ('TABLE REGULAR', 'TABLE REGULAR'),
        ('TABLE GLASS', 'TABLE GLASS'),
        ('DESK PUBLIC', 'DESK PUBLIC'),
        ('DESK CONSULTATION', 'DESK CONSULTATION'),
        ('DESK TALL', 'DESK TALL'),
        ('DESK OSX', 'DESK OSX'),
        ('DESK WIN', 'DESK WIN'),
        ('DESK OSX w/ SCANNER', 'DESK OSX w/ SCANNER'),
        ('DESK WIN w/ SCANNER', 'DESK WIN w/ SCANNER'),
        ('DESK LAPTOP', 'DESK LAPTOP'),
        ('TABLE BIG MAP', 'TABLE BIG MAP'),
    )
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=50)
    rfid = models.CharField(max_length=50, blank=False, null=False)
    furniture_type = models.CharField(max_length=25, choices=TYPES)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    unix_timestamp = models.IntegerField()
    created_by = models.CharField(max_length=25)
    latitude = models.FloatField(validators = [MinValueValidator(-90), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators = [MinValueValidator(-180.0), MaxValueValidator(180.0)])
    geom = models.PointField(srid=4326)
    #geom = models.PointField(srid=900913)

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.unix_timestamp = utils.unix_timestamp()
        if not self.uuid or "" == self.uuid:
            self.uuid = utils.long_uuid()
        if not self.rfid or "" == self.rfid:
            raise ValueError("rfid cannot be NULL")
        # if not self.longitude or self.latitude or "" == self.longitude or "" == self.latitude:  
        #   raise ValueError("Invalid Feature Geometry")
        self.geom = Point(
            float(self.longitude), 
            float(self.latitude)
        )
        #print(dir(self.geom))
        #print(self.geom.wkt)
        #print(self.geom.srid)
        #print(self.geom.crs)
        #print(self.geom.geom_type)
        #print(self.geom.geojson) # type == str
        #self.unix_timestamp = utils.unix_timestamp()
        super(Furniture, self).save()

    def toGeoJSON(self):
        return  { 
            "type": "Feature",
            "geometry": {
                "type": "Point", 
                "coordinates": [self.longitude, self.latitude]
            },
            "properties": {
                "uuid": self.uuid,
                "rfid": self.rfid,
                "furniture_type": self.furniture_type
            }
        }


class Person(models.Model):
    PERSON_TYPE = (
        ('ACADEMIC', 'ACADEMIC'),
        ('PUBLIC', 'PUBLIC'),
    )
    COMPUTER_TYPE = (
        ('DESKTOP', 'DESKTOP'),
        ('LAPTOP', 'LAPTOP'),
        ('NONE', 'NONE'),
    )
    id = models.AutoField(primary_key=True)
    person_type = models.CharField(max_length=25, choices=PERSON_TYPE)
    collab = models.BooleanField()
    computer_type = models.CharField(max_length=25, choices=COMPUTER_TYPE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    unix_timestamp = models.IntegerField()
    created_by = models.CharField(max_length=25)
    latitude = models.FloatField(validators = [MinValueValidator(-90), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators = [MinValueValidator(-180.0), MaxValueValidator(180.0)])
    geom = models.PointField(srid=4326)

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.unix_timestamp = utils.unix_timestamp()
        # if not self.longitude or self.latitude or "" == self.longitude or "" == self.latitude:  
        #   raise ValueError("Invalid Feature Geometry")
        self.geom = Point(
            float(self.longitude), 
            float(self.latitude)
        )
        #self.unix_timestamp = utils.unix_timestamp()
        super(Person, self).save()


class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=50)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    unix_timestamp = models.IntegerField()
    created_by = models.CharField(max_length=25)
    outlets_used = models.IntegerField()

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.unix_timestamp = utils.unix_timestamp()
        #self.unix_timestamp = utils.unix_timestamp()
        super(Zone, self).save()


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    unix_timestamp = models.IntegerField()
    created_by = models.CharField(max_length=25)
    messy = models.BooleanField()
    noise = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.unix_timestamp = utils.unix_timestamp()
        #self.unix_timestamp = utils.unix_timestamp()
        super(Room, self).save()



# from django.contrib.gis.geos import Point
# pnt = Point(12.4604, 43.9420)
# geom = models.PointField(srid=4326)


