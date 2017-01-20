#!/usr/bin/python
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.isfile('config.json'):
    config = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.spatialite',
            'NAME': os.path.join(BASE_DIR, 'geo.sqlite3'),
            'OPTIONS': {
                'timeout': 20
            }
        }
    }

    with open('config.json', 'w') as outfile:
        json.dump(config, outfile)

