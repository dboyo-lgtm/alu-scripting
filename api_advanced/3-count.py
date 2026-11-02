#!/usr/bin/python3
"""
Recursive module to count keywords in Reddit hot posts.
"""

import re
import requests


def count_words(subreddit, word_list, after=None, instances=None):
    """
    Recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords.
    """
    if instances is None:
        instances = {}
        # Normalize word_list to lowercase and deduplicate/initialize counts
        for word in word_list:
            w_lower = word.lower()
            instances[w_lower] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python:alu.api.advanced:v1.0'}
    params = {'after': after} if after else {}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json()
    children = data.get('data', {}).get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        # Extract exact words using word boundaries
        words_in_title = re.findall(r'\b[a-zA-Z0-9]+\b', title)
        for word in words_in_title:
            if word in instances:
                instances[word] += 1

    after = data.get('data', {}).get('after')
    if after:
        return count_words(subreddit, word_list, after, instances)

    # Base case / final processing: filter out 0 counts and sort results
    filtered = {k: v for k, v in instances.items() if v > 0}
    sorted_words = sorted(
        filtered.items(),
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_words:
        print("{}: {}".format(word, count))
