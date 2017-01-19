import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_default_db_config():
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

def get_db_config():
    # create base config
    if not os.path.isfile('config.json'):
        create_default_db_config()
    # read config file and return data
    data = {}
    with open('config.json', 'r') as infile:
        data = json.loads(infile.read())
    return data

