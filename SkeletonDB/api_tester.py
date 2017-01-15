import json
import requests

url = "http://localhost:8000/api/v1/set/stefan"
resp = requests.post(url, data=json.dumps({"test":123}))
print(resp)
print(resp.text)
