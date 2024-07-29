#!/usr/bin/python3
"""Rest API to fetch todo lists of employees"""

import json
import requests


if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(api_url)
    Users = resp.json()

    users_dict = {}
    for user in Users:
        id = user.get('id')
        username = user.get('username')
        api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        api_url = api_url + '/todos/'
        resp = requests.get(api_url)

        tasks = resp.json()
        users_dict[id] = []
        for task in tasks:
            status = task.get('completed')
            title = task.get('title')
            users_dict[id].append({
                "task": title,
                "completed": status,
                "username": username
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
