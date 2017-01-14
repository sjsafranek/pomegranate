#!/usr/bin/python

# Import the utility functions from the URL handling library
from django.conf.urls import url

# Import auth_views for login and logout methods
from django.contrib.auth import views as auth_views

from . import views
from . import api

urlpatterns = [
    url(r'^$', auth_views.login, { "template_name" : "login.html"}),
    url(r'^logout/$', auth_views.logout, { "next_page" : '/'}),
    url(r'^map$', views.map),
    url(r'^api/v1/zone$', api.zone_info),
    url(r'^api/v1/zones/export$', api.zone_export),
    url(r'^api/v2/zones/export$', api.zone_export_multithread)
]

