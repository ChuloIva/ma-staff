import praw
import pandas as pd
import datetime as dt

pd.options.display.max_columns = None
pd.options.display.width=None


reddit = praw.Reddit(client_id='gP1ZDwru6lQ7_Q', \
                     client_secret='HkdorTFcvI75e63hrHAo1ogjNtNriQ', \
                     user_agent='Scraping', \
                     username='hyperamper666', \
                     password='Jebemtiboga666')

subreddit = reddit.subreddit('wallstreetbets')

gains_list = subreddit.search("gains")

gains_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in gains_list:
    gains_dict["title"].append(submission.title)
    gains_dict["score"].append(submission.score)
    gains_dict["id"].append(submission.id)
    gains_dict["url"].append(submission.url)
    gains_dict["comms_num"].append(submission.num_comments)
    gains_dict["created"].append(submission.created)
    gains_dict["body"].append(submission.selftext)



gains_data = pd.DataFrame(gains_dict)
# print(gains_data)

from tabulate import tabulate

# print(tabulate(gains_data))

