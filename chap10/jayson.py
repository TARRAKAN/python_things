import json

nums = [1,1,2,3,5,8,13,21,34,55]

with open("numbers.json", 'w') as file:
    json.dump(nums, file)
