#!/usr/bin/python3
""" return top ten"""

import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        return None  # <-- Fix 1: return None (not print)

    json_data = response.json()
    posts = json_data.get('data', {}).get('children', [])

    if not posts:
        return None  # <-- Optional: handle empty subreddit

    for post in posts[:10]:
        print(post['data']['title'])  # <-- Print top 10 titles

    return 1  # <-- Fix 2: return something meaningful (e.g., 1 or True)
