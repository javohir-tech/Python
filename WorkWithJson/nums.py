import json

nums = [1, 2, 3, 4]
nums2 = [2, 3, 4, 5]

with open("../Data/nums.json", "w") as file:
    json.dump(nums, file)
