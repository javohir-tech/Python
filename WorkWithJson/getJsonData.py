import json

with open('../Data/bemor.json') as file :
    data = json.load(file)
    
print(data)