#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Returns the titles of the top ten hot posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    Url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user = {'User-Agent':
            'Python/requests:APIproject:v1 (by /u/rubenoliveros)'}
    payload = requests.get(Url, headers=user, params={'limit': 10}).json()
    posts = payload.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get('title', None))
