#!/usr/bin/python

import django.db.utils

# Import models
from .models import Zone
from .models import Furniture

def commit(obj):
    try:
        obj.save()
    except django.db.utils.OperationalError:
        commit(obj)
    except Exception as e:
        print(e)


