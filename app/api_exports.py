#!/usr/bin/python

# Import the login_required decorator which can be applied to views 
# to enforce that the user should be logged in to access the view
from django.contrib.auth.decorators import login_required

# Import csrf_exempt to bypass csrf protections for ajax requests
# TODO: Don't bypass csrf protections
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.http import JsonResponse

# Import models
from .models import Zone
from .models import Furniture
from .models import Person
from .models import Room

from . import utils

# Import standard modules for data parsing and responses
import csv
import json
import logging
#logger = logging.getLogger(__name__)

from .api_response import ApiResponse


@login_required(login_url='/')
def zone_export_csv(request):
    '''Returns csv file containing zone measurements'''

    if not request.user.is_authenticated():
        return JsonResponse(
            ApiResponse.not_authenticated(), 
            status=401)

    if not request.user.is_superuser:
        return JsonResponse(
            ApiResponse.unauthorized(), 
            status=401)

    if request.method == "GET":
		#job_id = utils.short_uuid()
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="zones.csv"'
        writer = csv.writer(response)
        writer.writerow([
            "id",
            "uuid",
            "outlets_used",
            "username",
            "unix_timestamp",
            "created_timestamp",
            "updated_timestamp"
        ])
        for row in Zone.objects.all():
            writer.writerow([
                row.id,
                row.uuid,
                row.outlets_used,
                row.username,
                row.unix_timestamp,
                row.created_timestamp,
                row.updated_timestamp
        ])
        return response

    return JsonResponse(
        ApiResponse.method_not_allowed(request.method, ["GET"]),
        status=400)




@login_required(login_url='/')
def furniture_export_csv(request):
    '''Returns csv file containing furniture measurements'''

    if not request.user.is_authenticated():
        return JsonResponse(
            ApiResponse.not_authenticated(), 
            status=401)

    if not request.user.is_superuser:
        return JsonResponse(
            ApiResponse.unauthorized(), 
            status=401)

    if request.method == "GET":
        #job_id = utils.short_uuid()
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="furniture.csv"'
        writer = csv.writer(response)
        writer.writerow([
            "id",
            "uuid",
            "rfid",
            "furniture_type",
            "latitude",
            "longitude",
            "username",
            "unix_timestamp",
            "created_timestamp",
            "updated_timestamp"
        ])
        for row in Furniture.objects.all():
            writer.writerow([
                row.id,
                row.uuid,
                row.rfid,
                row.furniture_type,
                row.latitude,
                row.longitude,
                row.username,
                row.unix_timestamp,
                row.created_timestamp,
                row.updated_timestamp
        ])
        return response

    return JsonResponse(
        ApiResponse.method_not_allowed(request.method, ["GET"]),
        status=400)


@login_required(login_url='/')
def furniture_export_geojson(request):
    '''Returns geojson containing last known furniture locations'''

    if not request.user.is_authenticated():
        return JsonResponse(
            ApiResponse.not_authenticated(), 
            status=401)

    if request.method == "GET":
        #job_id = utils.short_uuid()
        featureCollection =   {
            "type": "FeatureCollection",
            "features": []
        }
        
        features = Furniture.objects.order_by("unix_timestamp")
        features = features.reverse()
        uuids = []
        for feature in features:
            if feature.uuid not in uuids:
                uuids.append(feature.uuid)
                featureCollection["features"].append(feature.toGeoJSON());

        return JsonResponse({
            "status": "ok",
            "data": {
                "layer": featureCollection
            }
        })

    return JsonResponse(
        ApiResponse.method_not_allowed(request.method, ["GET"]),
        status=400)
