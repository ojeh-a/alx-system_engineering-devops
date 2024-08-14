#!/usr/bin/python3
"""
Defines a function that queries the Reddit API and returns the number of
subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get('data')
    subscribers = data.get('subscribers')
    return subscribers
