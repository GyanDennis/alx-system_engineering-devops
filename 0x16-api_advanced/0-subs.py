#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Query the Reddit API and return the number of subscribers for a given subreddit"""
    
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    print("API URL:", url)

    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'My user Agent 1.0'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    print("Response status code:", response.status_code)

    # Check if the request was successful and not redirected
    if response.status_code == 200:
        # Parse JSON response to extract number of subscribers
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        # Invalid subreddit or other error, return 0
        return 0
