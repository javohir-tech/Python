import json
from pprint import pprint

filename = "./Data/bemor.json"

with open(filename) as file:
    res = json.load(file)
    
pprint(res)