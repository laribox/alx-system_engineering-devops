#!/usr/bin/python3
'''
Rest API to fetch user todo list
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com/"


if __name__ == "__main__":
    user = requests.get(REST_API + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(REST_API + "todos",
                         params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for title in completed:
        print(f"\t {title}")
