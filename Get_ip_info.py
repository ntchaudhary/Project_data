import requests
from pprint import pprint

data =requests.get("https://ipinfo.io/")

dat=data.json()
pprint(dat)
