#!/usr/bin/python3
"""This module queries the Reddit API and prints
the tiltels of the first ten hotspots listed for a given subreddit"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"user-agent": "Google Chrome Version 115.0.5790.110"}

    params = {"limit": 10}

    res = requests.get(url, params=params, headers=headers,
                       allow_redirects=False)

    if res.status_code == 404:
        print("None")
        return
    results = res.json().get('data').get('children')
    [print(c.get("data".get("title"))for c in results)]
