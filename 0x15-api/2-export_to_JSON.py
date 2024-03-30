#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import requests
import sys
import json


def disp():
    name = ''
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    for respo in users.json():
        if respo.get('id') == int(sys.argv[1]):
            name = respo.get('username')
            break

    response = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    Line = []
    user_id = 0
    expo = []

    for re in response.json():
        if re.get('userId') == int(sys.argv[1]):
            user_id = re.get('userId')
            Line.append((re.get('title'), re.get('completed')))

    for task in Line:
        expo.append({"task": task[0], "completed": task[1],
                     "username": name})

    data = {str(sys.argv[1]): expo}
    with open(f"{user_id}.json", 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    disp()
