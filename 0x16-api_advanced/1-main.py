#!/usr/bin/env python3

import requests
import sys

def fetch_top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {'User-Agent': 'MyBot/1.0'}  # Provide a proper User-Agent header
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    except requests.exceptions.HTTPError as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        fetch_top_ten(sys.argv[1])
