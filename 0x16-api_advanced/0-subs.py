#!/usr/bin/python3
"""Script that fetches Number of subscribers for a subreddit"""

from sys import argv
import requests


def fetchSubs():
    """Fetches subreddit subcount"""
    if len(argv) < 2:
        return print("Usage: {} <subreddit>".format(argv[0]))

    url = 'https://www.reddit.com/r/{}/about.json'.format(argv[1])

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        print(response.json()['data']['subscribers'])
    else:
        return print(0)


if __name__ == '__main__':
    fetchSubs()
