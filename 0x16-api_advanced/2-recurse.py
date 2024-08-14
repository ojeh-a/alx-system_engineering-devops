#!/usr/bin/python3
"""
Defines a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    after = data.get('after')
    posts = data.get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
