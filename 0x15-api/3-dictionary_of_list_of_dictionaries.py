#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
import sys


users = requests.get('https://jsonplaceholder.typicode.com/users')

response = requests.get('https://jsonplaceholder.typicode.com/todos')

Line = []
expo = []
data = dict()

for user in users.json():
    for re in response.json():
        if user.get('id') == re.get('id'):
            Line.append((user.get('username'), re.get('title'),
                         re.get('completed')))
            for task in Line:
                expo.append({"username": task[0], "task": task[1],
                             "completed": task[2]})
            data[user.get('id')] = expo

with open('todo_all_employees.json', 'w') as file:
    json.dump(data, file, sort_keys=True)
