import json

with open('../Data/bemor.json') as file :
    data = json.load(file)
    
with open('../Data/nums.json') as file :
    nums = json.load(file)
    
print(data)
print(nums[0])