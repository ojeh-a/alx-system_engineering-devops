#!/usr/bin/python3

"""
top_ten module
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 10
    }
    response = get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get('data')
    posts = data.get('children')
    for post in posts:
        print(post.get('data').get('title'))
