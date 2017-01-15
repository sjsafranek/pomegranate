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

logger = logging.getLogger("api")

from .api_response import ApiResponse
# from . import database


@csrf_exempt
@login_required(login_url='/')
def zone_info(request):
    if request.method == "POST":
        if request.is_ajax:
            try:
                if request.user.is_authenticated():
                    # read post body for data
                    body = request.body.decode("utf-8") 
                    data = json.loads(body)
                    logger.debug(data)
                    zone = Zone.objects.create(
                                uuid = data["uuid"],
                                username = request.user.username,
                                outlets_used = data["outlets_used"]
                            )
                    zone.save()
                    # database.commit(zone)
                    logger.info('{} {} {}'.format(request.method, request.path, 200))
                    return JsonResponse(
                        ApiResponse.ok())
                
                else:
                    logger.warning('{} {} {}'.format(request.method, request.path, 401))
                    return JsonResponse(
                        ApiResponse.not_authenticated(), 
                        status=401)
            
            except Exception as e:
                logger.error('{} {} {}'.format(request.method, request.path, 500))
                return JsonResponse(
                    ApiResponse.fatal(e), 
                    status=500)
        #else:
            # TODO: handle web form
            # Stuff here
        #    return redirect('/map')

    logger.warning('{} {} {}'.format(request.method, request.path, 400))
    return JsonResponse(
        ApiResponse.method_not_allowed(request.method, ["POST"]),
        status=400)


@csrf_exempt
@login_required(login_url='/')
def room_info(request):
    if request.method == "POST":
        if request.is_ajax:
            try:
                if request.user.is_authenticated():
                    # read post body for data
                    body = request.body.decode("utf-8") 
                    data = json.loads(body)
                    logger.debug(data)
                    room = Room.objects.create(
                                uuid = data["uuid"],
                                username = request.user.username,
                                messy = data["messy"],
                                noise = data["noise"]
                            )
                    room.save()
                    # database.commit(room)
                    logger.info('{} {} {}'.format(request.method, request.path, 200))
                    return JsonResponse(
                        ApiResponse.ok())
                
                else:
                    logger.warning('{} {} {}'.format(request.method, request.path, 401))
                    return JsonResponse(
                        ApiResponse.not_authenticated(), 
                        status=401)
            
            except Exception as e:
                logger.error('{} {} {}'.format(request.method, request.path, 500))
                return JsonResponse(
                    ApiResponse.fatal(e), 
                    status=500)

    logger.warning('{} {} {}'.format(request.method, request.path, 400))
    return JsonResponse(
        ApiResponse.method_not_allowed(request.method, ["POST"]),
        status=400)


@csrf_exempt
@login_required(login_url='/')
def person_info(request):
    if request.method == "POST":
        if request.is_ajax:
            try:
                if request.user.is_authenticated():
                    # read post body for data
                    body = request.body.decode("utf-8") 
                    data = json.loads(body)
                    logger.debug(data)
                    person = Person.objects.create(
                                username = request.user.username,
                                person_type = data["person_type"],
                                collab = data["collab"],
                                computer_type = data["computer_type"],
                                latitude = data["latitude"],
                                longitude = data["longitude"]
                            )
                    person.save()
                    # database.commit(person)
                    logger.info('{} {} {}'.format(request.method, request.path, 200))
                    return JsonResponse(
                        ApiResponse.ok())
                
                else:
                    logger.warning('{} {} {}'.format(request.method, request.path, 401))
                    return JsonResponse(
                        ApiResponse.not_authenticated(), 
                        status=401)
            
            except Exception as e:
                logger.error('{} {} {}'.format(request.method, request.path, 500))
                return JsonResponse(
                    ApiResponse.fatal(e), 
                    status=500)

    logger.warning('{} {} {}'.format(request.method, request.path, 400))
    return JsonResponse(
        ApiResponse.method_not_allowed(request.method, ["POST"]),
        status=400)


@csrf_exempt
@login_required(login_url='/')
def furniture_info(request):
    if request.method == "POST":
        if request.is_ajax:
            try:
                if request.user.is_authenticated():
                    # read post body for data
                    body = request.body.decode("utf-8") 
                    data = json.loads(body)
                    logger.debug(data)
                    furniture = Furniture.objects.create(
                                uuid = data["uuid"],
                                username = request.user.username,
                                furniture_type = data["furniture_type"],
                                rfid = data["rfid"],
                                latitude = data["latitude"],
                                longitude = data["longitude"]
                            )
                    furniture.save()
                    # database.commit(furniture)
                    logger.info('{} {} {}'.format(request.method, request.path, 200))
                    return JsonResponse(
                        ApiResponse.ok())
                
                else:
                    logger.warning('{} {} {}'.format(request.method, request.path, 401))
                    return JsonResponse(
                        ApiResponse.not_authenticated(), 
                        status=401)
            
            except Exception as e:
                logger.error('{} {} {}'.format(request.method, request.path, 500))
                return JsonResponse(
                    ApiResponse.fatal(e), 
                    status=500)

    logger.warning('{} {} {}'.format(request.method, request.path, 400))
    return JsonResponse(
        ApiResponse.method_not_allowed(request.method, ["POST"]),
        status=400)

