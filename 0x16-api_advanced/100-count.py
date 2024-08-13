#!/usr/bin/python3
"""Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    Queries the Reddit API, parses the titles of all hot articles, and prints
    a sorted count of given keywords (case-insensitive, delimited by spaces).
    
    - Javascript should count as javascript, but java should not.
    - If no posts match or the subreddit is invalid, it prints nothing.
    """

    if word_dict is None:
        word_dict = {}
        for word in word_list:
            word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in wordict:
            if count > 0:
                print(f'{word}: {count}')
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json().get('data', {})
        hot_posts = data.get('children', [])
        after = data.get('after', None)

        for post in hot_posts:
            title = post['data'].get('title', '').lower().split()
            for word in word_dict:
                word_dict[word] += title.count(word)

    except (ValueError, KeyError):
        return

    count_words(subreddit, word_list, after, word_dict)

