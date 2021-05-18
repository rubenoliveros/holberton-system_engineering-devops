#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of total subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    Url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = {'User-Agent':
            'Python/requests:APIproject:v1 (by /u/rubenoliveros)'}
    payload = requests.get(Url, headers=user).json()
    subscribers = payload.get("data", {}).get("subscribers", 0)
    return subscribers
