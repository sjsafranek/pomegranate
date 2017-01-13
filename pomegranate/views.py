from django.shortcuts import render


# Import redirect and render shortcuts
from django.shortcuts import redirect
from django.shortcuts import render_to_response

# Import reverse_lazy method for reversing names to URLs
from django.core.urlresolvers import reverse_lazy

# Import the login_required decorator which can be applied to views 
# to enforce that the user should be logged in to access the view
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt


from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth.models import User
# from django.contrib.auth.models import Group
from django.contrib.auth.hashers import check_password

from .models import Zone
from .models import Furniture

import json

# Create your views here.
# @login_required(login_url='/')
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# My hacky way of doing Jinja2 rendering because
# Django Jinja2 GIVES NO ERROR OUTPUT WHEN SOMETHING GOES WRONG - it just quits
# so fuck that. - Zack Scholl
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('sarah_app/templates'))

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

@login_required(login_url='/')
def map(request):
    if request.user.is_authenticated():
        username = request.user.username
        # return HttpResponse("Hello, world. You are logged in as " + username + ".")
        return render(request, "map.html", {"username":username})

