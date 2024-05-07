#!/usr/bin/python3
"""Script that fetches Number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries REDDIT API and fetches subreddit subcount

    Args:
        subreddit (str): the given subreddit

    Returns:
        int: returns the subcount otherwise 0 if invalid
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
