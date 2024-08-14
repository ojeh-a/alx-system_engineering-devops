#!/usr/bin/python3

"""
top_ten module
"""

from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    for post in response.json().get('data').get('children'):
        print(post.get('data').get('title'))
