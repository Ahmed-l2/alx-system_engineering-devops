#!/usr/bin/python
"""Script that fetches Number of subscribers for a subreddit"""

import requests
from sys import argv


def fetchSubs():
    """Fetches subreddit subcount"""
    if len(argv) < 2:
        return "Usage: {} <subreddit>".format(argv[0])

    url = 'https://www.reddit.com/r/{}/about.json'.format(argv[1])

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        print(response.json()['data']['subscribers'])
    else:
        return 0


if __name__ == '__main__':
    fetchSubs()
