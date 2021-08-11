import json

with open("numbers.json", 'r') as file:
    numbers = json.load(file)

print(numbers)
