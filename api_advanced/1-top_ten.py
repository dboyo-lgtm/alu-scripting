#!/usr/bin/python3
"""
Module to query Reddit API and print the
titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the
    titles of the first 10 hot posts.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit
    )
    headers = {'User-Agent': 'python:alu.api.advanced:v1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get('data', {}).get('title'))
            return
        except ValueError:
            pass

    print(None)
