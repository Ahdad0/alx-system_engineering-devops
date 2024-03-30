#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import requests
import sys


def disp():
    name = ''
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    for respo in users.json():
        if respo.get('id') == int(sys.argv[1]):
            name = respo.get('name')
            break

    response = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    Line = ''
    user_id = 0
    statu = None
    title = ''

    for re in response.json():
        if re.get('userId') == int(sys.argv[1]):
            user_id = re.get('userId')
            statu = re.get('completed')
            title = re.get('title')
            Line = f'"{user_id}","{name}","{statu}","{title}"'
            append_to_file(user_id, Line)


def append_to_file(user_id, line):
    with open(f"{user_id}.csv", 'a') as file:
        file.write(line + '\n')


if __name__ == '__main__':
    disp()
