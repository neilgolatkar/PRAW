'''
Created on Nov 29, 2018

@author: Neil Golatkar
'''
import praw
from praw.models.listing.mixins import submission
"""Input your own credentials, client secret, and client id here"""
reddit = praw.Reddit(client_id='Client ID',
                     client_secret='Client Secret', password='Password',
                     user_agent='Your User Agent', username='Insert Your Username Here')

"""Check to see if your credentials worked"""
print(reddit.user.me())

"Insert subreddits to take posts from"
fix_posts = reddit.subreddit('subreddits to take posts from').hot
for submission in fix_posts(limit=5):
    if not submission.stickied:
        link=submission.url
        "Debug if link works"
        "print(link)"
        title=submission.title
        "Debug if title works. Will throw error if non unicode in title"
        "print(title)"
        "Input subreddit to post to"
        reddit.subreddit('Subreddit to Post to').submit(title, url=link)
