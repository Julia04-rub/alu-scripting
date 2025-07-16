#!/usr/bin/python3
"""Return top 10 hot post titles for a subreddit"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None  # Required when subreddit is invalid

    data = response.json().get("data", {}).get("children", [])

    for post in data[:10]:
        print(post.get("data", {}).get("title"))

    return "OK"  # <- Required when subreddit is valid

