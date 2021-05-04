#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from sys import argv
import requests

if __name__ == '__main__':
    Id = argv[1]
    USERGETURL = "https://jsonplaceholder.typicode.com/users/{}".format(Id)
    user = requests.get(USERGETURL).json()
    TASKGETURL = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(Id)
    user_tasks = requests.get(TASKGETURL).json()
    tasks_done = []
    for task in user_tasks:
        if task.get('completed') is True:
            tasks_done.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                          len(tasks_done),
                                                          len(user_tasks)))
    for i in tasks_done:
        print("\t {}".format(i))
