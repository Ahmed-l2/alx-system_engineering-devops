#!/usr/bin/python3
"""Script that fetches Number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Fetches subreddit subcount"""

    if not subreddit or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
