#!/usr/bin/env python

import sys
import json
import requests

if 3 != len(sys.argv):
	ValueError("Incorrect usage")

url = "http://localhost:8000/api/v1/set/{}".format(sys.argv[1])
resp = requests.post(url, data=sys.argv[2])

print(resp.text)
