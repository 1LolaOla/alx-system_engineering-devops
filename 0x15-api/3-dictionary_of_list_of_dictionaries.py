#!/usr/bin/python3
"""
Export data in JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    todo_dict = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for todo in todos:
            if todo.get("userId") == user_id:
                task = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
                tasks.append(task)
        todo_dict[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_dict, json_file)
