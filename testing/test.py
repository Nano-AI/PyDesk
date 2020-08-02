import requests

with requests.get('../config/settings.json').json() as f:
    print(f)
