#!/usr/bin/python3
"""Script that fetches Number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Fetches subreddit subcount"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
