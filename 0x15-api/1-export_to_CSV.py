#!/usr/bin/python3
''' export data in the CSV format '''

from requests import get
import csv
from sys import argv

if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com'
    usr = get(endpoint + '/users/' + argv[1]).json()['username']
    todos = get(endpoint + '/todos?userId=' + argv[1]).json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], usr, todo['completed'], todo['title']]
