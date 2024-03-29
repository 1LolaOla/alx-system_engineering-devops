#!/usr/bin/python3
<<<<<<< HEAD
"""Advanced Apis Module"""
import requests
import sys


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given,
    the function should return 0."""

    headers = {"User-Agent": "user_agent"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(
=======
"""
Queries the Reddit API and returns number of subscrbers
not active users, total subscribers for a given subreddit
If an invalid subreddit is given, the function returns 0.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    not active users, total subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """

    headers = {"User-Agent": "user_agent"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(   
>>>>>>> af893637cc2a9df47d14df44cb1d79c3ea69b668
        url=url,
        headers=headers,
        allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        subscribers = data['subscribers']
        return (subscribers)
    else:
        return (0)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subred = sys.argv[1]
        number_of_subscribers(subred)
