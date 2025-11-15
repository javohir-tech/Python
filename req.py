import requests
import pprint

manzil = "https://kun.uz/news/main"
res = requests.get(manzil)
pprint.pprint(res.text)

# country = "Uzbekistan"
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# res = requests.get(url)
# print(res.status_code)
# r_json = res.json()
# print(r_json)