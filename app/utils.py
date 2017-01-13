#!/usr/bin/python

import time
import datetime

def unix_timestamp():
	return int(time.mktime(datetime.datetime.utcnow().timetuple()))
