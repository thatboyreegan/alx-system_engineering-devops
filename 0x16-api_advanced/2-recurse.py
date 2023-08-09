#!/usr/bin/python3
"""This module queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"user-agent": "Google Chrome Version 115.0.5790.110"}

    params = {
        "limit": 100,
        "count": count,
        "after": after
    }

    res = requests.get(url, params=params, headers=headers,
                       allow_redirects=False)

    if res.status_code == 404:
        return None

    results = res.json().get('data')
    after = results.get('after')
    count += results.get('dist')

    for c in results.get('children'):
        hot_list.append(c.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, after, hot_list, count)
    return hot_list
