import requests
import json

url_endpoint = "http://127.0.0.1:5000/generator"
resp = requests.get(url_endpoint, params = {"message" : "woa",
                                            "capitalization":"UPPER",
                                            "duplication_factor":3})

print(resp.json())
print(resp.status_code)