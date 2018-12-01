import praw
import re
"""import random
import time
import os"""

meme_words = ["tracer"]

reddit = praw.Reddit(client_id='lEu29A23e5Sq1A',
                     client_secret='vU-XixIIg4UBTY22N0HcTHMuhNY', password='pokemon10',
                     user_agent='Tracer_Bot 1.0', username='ANAL_DRAWSTRINGS')

print(reddit.user.me())
"""if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
        """

subreddit = reddit.subreddit("Overwatch")
for comment in subreddit.stream.comments():
    print(comment.body.encode("utf-8"))
    if re.search("tracer", comment.body):
        tracer_reply = "I'm already Tracer!"
        comment.reply(tracer_reply)
        print(tracer_reply)