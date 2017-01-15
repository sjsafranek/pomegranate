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
def zone_export(request):
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
            "created_timestamp",
            "updated_timestamp",
            "username",
            "outlets_used",
            "unix_timestamp"])
        for zone in Zone.objects.all():
            writer.writerow([
                zone.id,
                zone.uuid,
                zone.created_timestamp,
                zone.updated_timestamp,
                zone.username,
                zone.outlets_used,
                zone.unix_timestamp])
        return response
