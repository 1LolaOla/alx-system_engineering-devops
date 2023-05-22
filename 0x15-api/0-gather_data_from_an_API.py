#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    # Fetch user information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch user's todo list
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    # Print progress information
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
