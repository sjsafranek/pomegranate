#!/usr/bin/python

# Import the utility functions from the URL handling library
from django.conf.urls import url

# Import auth_views for login and logout methods
from django.contrib.auth import views as auth_views

from . import views
from . import api_imports
from . import api_exports
from . import apiV2

urlpatterns = [
    url(r'^$', auth_views.login, { "template_name" : "login.html"}),
    url(r'^logout/$', auth_views.logout, { "next_page" : '/'}),
    url(r'^map$', views.map),
    url(r'^api/v1/zone$', api_imports.zone_info),
	url(r'^api/v1/room$', api_imports.room_info),
	url(r'^api/v1/furniture$', api_imports.furniture_info),
	url(r'^api/v1/person$', api_imports.person_info),
    url(r'^api/v1/zones/export$', api_exports.zone_export),
    url(r'^api/v1/furniture/export$', api_exports.furniture_export),
    url(r'^api/v2/zones/export$', apiV2.zone_export_multithread)
]
