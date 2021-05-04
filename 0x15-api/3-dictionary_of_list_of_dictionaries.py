#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import json
import requests

if __name__ == '__main__':
    USERGETURL = "https://jsonplaceholder.typicode.com/users"
    all_users = requests.get(USERGETURL).json()
    TASKGETURL = "https://jsonplaceholder.typicode.com/todos"
    all_user_tasks = requests.get(TASKGETURL).json()
    dict_to_json = {}
    for user in all_users:
        list_to_json = []
        for task in all_user_tasks:
            t_dict = {}
            t_dict["username"] = user.get('username')
            t_dict["task"] = task.get('title')
            t_dict["completed"] = task.get('completed')
            list_to_json.append(t_dict)
        dict_to_json = {user.get('id'): list_to_json}
    with open("todo_all_employees.json", 'w') as filej:
        json.dump(dict_to_json, filej)
