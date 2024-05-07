#!/usr/bin/python3
"""Script that fetches Number of subscribers for a subreddit"""
import requests
import sys


def top_ten(subreddit):
    """Fetches subreddit subcount"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    header = {'User-Agent': 'Chrome'}
    limit = {'limit': 10}
    response = requests.get(url, headers=header, params=limit,
                            allow_redirects=False)

    if response.status_code == 200:
        for post in response.json()['data']['children']:
            print(post['data']['title'])
    else:
        return 0


if __name__ == "__main__":
    top_ten(sys.argv[1])
