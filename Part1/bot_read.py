#!/usr/bin/python
import praw

user_agent = ("picklebot9000")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("calgaryflames")

for submission in subreddit.get_hot(limit = 5):
    print "Title: ", submission.title
    print "Text: ", submission.selftext
    print "Score: ", submission.score
    print "---------------------------------\n"
