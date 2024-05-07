#!/usr/bin/python3
"""Fetches Reddit API"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """Fetches Reddit API to return the list of hot posts in given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    header = {'User-Agent': 'Python Reddit API Client'}
    params = {"after": after}
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        hot_posts = response.json()['data']['children']
        for post in hot_posts:
            title = post['data']['title']
            hot_list.append(title)

        next_page = response.json()['data']['after']
        if next_page:
            return recurse(subreddit, hot_list, after=next_page)
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    recurse(sys.argv[1])
