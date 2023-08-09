#!/usr/bin/python3
"""This module querries the Reddit API and returns the number of
subcribers for a given subreddit or 0 if the subreddit provided is invalid"""

import requests


def number_of_subscribers(subreddit):

    b_url = f'http://reddit.com/r/{subreddit}/about.json'

    headers = {'user_agent': 'Google Chrome Version 115.0.5790.110'}

    res = requests.get(b_url, headers=headers, allow_redirects=False)

    if res.status_code in [302, 404]:
        return 0
    return res.json().get('data').get('subscbers')
