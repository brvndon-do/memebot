# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import praw
import json

from pprint import pprint
from dotenv import load_dotenv

class SearchReddit:
    def __init__(self):
        load_dotenv()
        self.reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), 
                        client_secret=os.getenv('CLIENT_SECRET'), 
                        user_agent=os.getenv('USER_AGENT'), 
                        username=os.getenv('USERNAME'), 
                        password=os.getenv('PASSWORD'))

    def get_data(self):
        for submission in self.reddit.subreddit('me_irl').top(limit=1):
            return submission.url


def main():
    #r = SearchReddit()
    #print(r.get_data())

    load_dotenv()
    reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), 
                client_secret=os.getenv('CLIENT_SECRET'), 
                user_agent=os.getenv('USER_AGENT'), 
                username=os.getenv('USERNAME'), 
                password=os.getenv('PASSWORD'))

    for submission in reddit.subreddit('me_irl').hot(limit=5):
        pprint(vars(submission))


if __name__ == '__main__':
    main()