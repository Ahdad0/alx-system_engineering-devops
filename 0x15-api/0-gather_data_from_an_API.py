#!/usr/bin/python3

"""
Write a Python script that, using this REST API
for a given employee ID, returns information
about his/her TODO list progres
"""
import requests
import sys


EMPLOYEE_NAME = ''
response_users = requests.get(f'https://jsonplaceholder.typicode.com/users')
for respo in response_users.json():
    if respo.get('id') == int(sys.argv[1]):
        EMPLOYEE_NAME = respo.get('username')
        break

response = requests.get(f'https://jsonplaceholder.typicode.com/todos')

TOTAL_NUMBER_OF_TASKS = 0
NUMBER_OF_DONE_TASKS = 0
TASK_TITLE = []

for re in response.json():
    if re.get('userId') == int(sys.argv[1]):
        TOTAL_NUMBER_OF_TASKS += 1
        if re.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(re.get('title'))

print('Employee {} is done with tasks({}/ {}):'
      .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
for t in TASK_TITLE:
    print('\t {}'.format(t))
