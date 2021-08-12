import json

filename = "username.json"
try:
    with open(filename) as file:
        username = json.load(file)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as file:
        json.dump(username, file)
        print("We'll remember you when you come back, " + username + '!')
else:
    print("Welcome back, " + username + '!')
