#!/usr/bin/python3
'''
Rest API to fetch user todo list
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def fetch_user_todo_list(user_id):
    user = requests.get(f"{REST_API}/users/{user_id}").json()
    todos = requests.get(f"{REST_API}/todos?userId={user_id}").json()

    user_name = user.get('name')
    completed_tasks = [task for task in todos if task.get('completed')]

    print(f"Employee {user_name} is done with "
          f"tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        fetch_user_todo_list(int(sys.argv[1]))
