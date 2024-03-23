#!/usr/bin/env python3

import requests
import sys

def fetch_posts(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    posts = set()  # Using a set to store unique posts
    for post in data['data']['children']:
        posts.add(post['data']['title'])
    return posts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)
    subreddit = sys.argv[1]
    posts = fetch_posts(subreddit)
    for post in posts:
        print(post)
