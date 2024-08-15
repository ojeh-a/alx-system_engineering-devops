#!/usr/bin/python3
"""
Defines a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""

import requests
import sys
import re


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively queries the Reddit API for hot articles in a given subreddit
    and tallies the count of words in the titles of the articles
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get('data')
    after = data.get('after')
    posts = data.get('children')
    for post in posts:
        title = post.get('data').get('title')
        title_words = re.split(r'\W+', title)
        for word in title_words:
            word = word.lower()
            if word in word_list:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    if after is not None:
        count_words(subreddit, word_list, word_count, after)
    else:
        if not word_count:
            return
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print('{}: {}'.format(word, count))
