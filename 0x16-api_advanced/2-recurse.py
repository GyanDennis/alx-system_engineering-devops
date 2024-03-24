#!/usr/bin/python3
"""Function to retrieve a list of all hot posts on a given Reddit subreddit."""

import requests

def get_hot_posts(subreddit, hot_list=[], after=None, count=0):
    """
    Retrieve a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot posts.
        after (str): A token for pagination to retrieve the next set of results.
        count (int): The count of posts retrieved so far.

    Returns:
        list: A list containing the titles of all hot posts on the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error: Failed to retrieve hot posts from {subreddit}. Status code: {response.status_code}")
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after:
        return get_hot_posts(subreddit, hot_list, after, count)
    return hot_list

# Example usage:
if __name__ == "__main__":
    subreddit_name = "programming"
    hot_posts = get_hot_posts(subreddit_name)
    if hot_posts:
        print(f"Hot posts on r/{subreddit_name}:")
        for i, post in enumerate(hot_posts, start=1):
            print(f"{i}. {post}")
    else:
        print("Failed to retrieve hot posts.")
