import praw
import re


meme_words = [""]

"""Input your own credentials, client secret, and client id here"""
reddit = praw.Reddit(client_id='Client ID',
                     client_secret='Client Secret', password='Password',
                     user_agent='Your User Agent', username='Insert Your Username Here')

print(reddit.user.me())


subreddit = reddit.subreddit("Subreddit name")
for comment in subreddit.stream.comments():
    print(comment.body.encode("utf-8"))
    if re.search("Comment to search for", comment.body):
        tracer_reply = "Your comment here"
        comment.reply(tracer_reply)
        print(tracer_reply)
