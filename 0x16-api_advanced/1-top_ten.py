#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "user_agent"}
    response = requests.get(
        url=url,
        headers=headers,
        allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        for child in children:
            title = child['data']['title']
            print(title)
    else:
        print("None")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subred = sys.argv[1]
        top_ten(subred)
