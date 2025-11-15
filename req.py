import requests
import pprint

manzil = "https://kun.uz/news/main"
res = requests.get(manzil)
pprint.pprint(res.text)