#!/usr/bin/python3
"""
Queries the Reddit API and returns number of subscrbers
not active users, total subscribers for a given subreddit
If an invalid subreddit is given, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    not active users, total subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
    return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print(number_of_subscribers(sys.argv[1]))

