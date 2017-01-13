#!/usr/bin/python

# Import redirect and render shortcuts
#from django.shortcuts import redirect

# Import reverse_lazy method for reversing names to URLs
# from django.core.urlresolvers import reverse_lazy

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

from . import utils

# Import standard modules for data parsing and responses
import csv
import json

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
'''
Logging -
    logger.debug()
    logger.info()
    logger.warning()
    logger.error()
    logger.critical()
'''

@csrf_exempt
@login_required(login_url='/')
def zone_info(request):
    # check request for validity
    # if request.method == "GET":
    if request.method == "POST":
        if request.is_ajax:
            try:
                if request.user.is_authenticated():
                    # read post body for data
                    body = request.body.decode("utf-8") 
                    data = json.loads(body)
                    # get username
                    username = request.user.username
                    # create new zone to store data
                    zone = Zone.objects.create(
                                uuid = data["uuid"],
                                name = data["name"],
                                # username=request.POST["username"]
                                username = username,
                                state = data["state"],
                                noise = data["noise"],
                                users = data["users"],
                                outlets = data["outlets"],
                                collab = data["collab"],
                                laptops = data["laptops"],
                                furniture_moved = data["furniture_moved"],
                                unix_timestamp = utils.unix_timestamp()
                                # owner=group
                            )
                    zone.save()
                    return JsonResponse({"status":"ok"})
                else:
                    return JsonResponse({"status":"fail","data":{"error":"please login"}})
            except Exception as e:
                print(e)
                return JsonResponse({"status":"fail", "data":{}})
        else:
            # TODO: handle web form
            # Stuff here
            return redirect('/map')

    return JsonResponse({"status":"fail"})


@login_required(login_url='/')
def zone_export(request):
    '''Returns csv file containing zone measurements'''
    # TODO: superuser only!!
    if request.method == "GET":

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="zones.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "id",
            "uuid",
            "name",
            "created_timestamp",
            "updated_timestamp",
            "username",
            "state",
            "noise",
            "users",
            "outlets",
            "collab",
            "laptops",
            "furniture_moved",
            "unix_timestamp"])

        for zone in Zone.objects.all():
            writer.writerow([
                zone.id,
                zone.uuid,
                zone.name,
                zone.created_timestamp,
                zone.updated_timestamp,
                zone.username,
                zone.state,
                zone.noise,
                zone.users,
                zone.outlets,
                zone.collab,
                zone.laptops,
                zone.furniture_moved,
                zone.unix_timestamp])

        return response

