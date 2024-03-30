#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
import sys


users = requests.get('https://jsonplaceholder.typicode.com/users')

response = requests.get('https://jsonplaceholder.typicode.com/todos')

data = dict()

for user in users.json():
    expo = []
    for re in response.json():
        if user['id'] == re['userId']:
            expo.append({"username": user['username'], "task": re['title'],
                         "completed": re['completed']})
    data[str(user['id'])] = expo

with open('todo_all_employees.json', 'w') as file:
    json.dump(data, file, sort_keys=True)
