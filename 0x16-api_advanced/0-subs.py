#!/usr/bin/python3
"""Script that fetches Number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Fetches subreddit subcount"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    header = {'User-Agent': 'Chrome'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code >= 300:
        return 0
    return response.json()['data']['subscribers']

if __name__ == "__main__":
    number_of_subscribers(argv[1])
