#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from sys import argv
import json
import requests

if __name__ == '__main__':
    Id = argv[1]
    USERGETURL = "https://jsonplaceholder.typicode.com/users/{}".format(Id)
    user = requests.get(USERGETURL).json()
    TASKGETURL = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(Id)
    user_tasks = requests.get(TASKGETURL).json()
    list_to_json = []
    for task in user_tasks:
        t_dict = {}
        t_dict["task"] = task.get('title')
        t_dict["completed"] = task.get('completed')
        t_dict["username"] = user.get('username')
        list_to_json.append(t_dict)
    dict_to_json = {str(Id): list_to_json}
    with open("{}.json".format(Id), 'w') as filej:
        json.dump(dict_to_json, filej)
