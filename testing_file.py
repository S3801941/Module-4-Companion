import pprint
import requests

r = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
pprint.pprint(r.json())
url = "https://icanhazdadjoke.com/"
r = requests.get(url, headers={"Accept": "application/json"})
print(r.request.headers.get("Accept"))

format(r.json())