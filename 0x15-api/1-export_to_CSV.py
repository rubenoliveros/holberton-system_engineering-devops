#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from sys import argv
import csv
import requests

if __name__ == '__main__':
    Id = argv[1]
    USERGETURL = "https://jsonplaceholder.typicode.com/users/{}".format(Id)
    user = requests.get(USERGETURL).json()
    TASKGETURL = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(Id)
    user_tasks = requests.get(TASKGETURL).json()
    with open("{}.csv".format(Id), 'w', newline='') as filecsv:
        writer = csv.writer(filecsv, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            writer.writerow([int(Id),
                             user.get('name'),
                             task.get("completed"),
                             task.get('title')])
