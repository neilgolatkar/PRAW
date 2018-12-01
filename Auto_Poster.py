'''
Created on Nov 29, 2018

@author: Neil Golatkar
'''
import praw
from praw.models.listing.mixins import submission

reddit = praw.Reddit(client_id='VFcod8os0W8ybg',
                     client_secret='aS1jDJrU3ag_MEaMldhz1aAlgog', password='pokemon10',
                     user_agent='Test Auto_Poster v1', username='ANAL_DRAWSTRINGS')

print(reddit.user.me())

subreddit=reddit.subreddit('ass+mooning+asstastic')
fix_posts = reddit.subreddit('ass+mooning+asstastic').hot
top_posts = fix_posts
for submission in top_posts(limit=5):
    if not submission.stickied:
        link=submission.url
        "print(link)"
        title=submission.title
        "print(title)"
        reddit.subreddit('NSFW_ASS').submit(title, url=link)