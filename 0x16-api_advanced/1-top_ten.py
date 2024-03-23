#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("Invalid subreddit name.")
        return

    user_agent = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    params = {'limit': 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    try:
        response = requests.get(url, headers=user_agent, params=params)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except (KeyError, ValueError) as e:
        print(f"Failed to parse the response: {e}")


# Example usage
top_ten('programming')
