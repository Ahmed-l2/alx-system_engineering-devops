#!/usr/bin/python3
"""Fetches Reddit API"""
import requests
import sys
from collections import Counter


def count_words(subreddit, word_list, after=None, count_dict=None):
    """Fetches Reddit API to return the list of hot posts in given subreddit"""

    if not count_dict:
        count_dict = Counter()

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    header = {'User-Agent': 'Python Reddit API Client'}
    params = {"limit": 100, "after": after} if after else {"limit": 100}
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        hot_posts = response.json()['data']['children']
        for post in hot_posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    count_dict[word] += 1

        next_page = response.json()['data']['after']
        if next_page:
            return count_words(subreddit, word_list, after=next_page,
                               count_dict=count_dict)
        else:
            for word, count in count_dict.items():
                print("{}: {}".format(word, count))
    else:
        return
