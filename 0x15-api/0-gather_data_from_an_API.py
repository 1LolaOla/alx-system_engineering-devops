#!/usr/bin/python3
"""
using a REST API, retrieve info about an employee's TODO list
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.
    """
    # API endpoint URL
    url = 'https://jsonplaceholder.typicode.com'

    # Retrieve employee information
    response_user = requests.get(f'{url}/users/{employee_id}')
    response_todos = requests.get(f'{url}/todos?userId={employee_id}')

    # Check if employee exists
    if response_user.status_code != 200:
        print('Employee not found.')
        return

    # Get employee name
    employee_name = response_user.json().get('name')

    # Get employee's TODO list
    todos = response_todos.json()

    # Count completed tasks
    completed_tasks = [task for task in todos if task.get('completed')]

    # Display progress
    print(f'Employee {employee_name} is done with tasks'
          f'({len(completed_tasks)}/{len(todos)}):')

    # Display completed task titles
    for task in completed_tasks:
        print('\t', task.get('title'))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(int(employee_id))
