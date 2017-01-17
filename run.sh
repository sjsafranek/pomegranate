#!/bin/bash
set +x
cd /vagrant
/usr/bin/python3 manage.py runserver 0.0.0.0:8080
