#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and counts the occurrence of given keywords.
    Prints the sorted count of keywords in descending order by count.
    """

    if after is None:
        word_list = [word.lower() for word in word_list]
        word_count = {word: 0 for word in word_list}

    url = "https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for post in children:
                    title = post.get("data", {}).get("title")
                    if title:
                        for word in word_list:
                            count = title.lower().split().count(word)
                            word_count[word] += count
                after = data.get("after")
                if after:
                    return count_words(subreddit, word_list, after, word_count)
    sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_count:
        if count > 0:
            print(f"{word}: {count}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)

