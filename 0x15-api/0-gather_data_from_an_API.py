#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))

    # Get the to-do list for the employee using the provided employee ID
    user = user_response.json()
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    completed = []

    # Filter completed tasks and count them
    for t in todos:
        if t.get("completed") is True:
            completed.append(todo.get("title"))

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with indentation
    for complete in completed:
        print("\t {}".format(complete))

