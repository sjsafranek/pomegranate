#!/usr/bin/python

import os
import base64
import uuid
import time
import datetime

def unix_timestamp():
    return int(time.mktime(datetime.datetime.utcnow().timetuple()))

def short_uuid():
    return base64.b64encode(os.urandom(6)).decode("utf-8")

def medium_uuid():
    return base64.b64encode(str(time.time())).decode("utf-8")

def long_uuid():
	return str(uuid.uuid4())
	#return str(uuid.uuid4())[:8]

