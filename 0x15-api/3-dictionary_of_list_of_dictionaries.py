#!/usr/bin/python3
"""Fetch data"""
import json
import requests
from sys import argv


def fetch_data():
    """Fetch employee data from rest api"""

    data = {}
    todos = "https://jsonplaceholder.typicode.com/todos"
    users = "https://jsonplaceholder.typicode.com/users"

    user_list = requests.get(users).json()
    todo_list = requests.get(todos).json()

    for user in user_list:
        task_list = []
        for key in todo_list:
            if key['userId'] == user['id']:
                task = {"task": key['title'], "completed": key['completed'],
                        "username": user['username']}
                task_list.append(task)

        data[str(user['id'])] = task_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    fetch_data()
