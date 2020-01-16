# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import praw
import requests
import random
from dotenv import load_dotenv
from prawcore import NotFound

class RedditSearcher:
    def __init__(self):
        load_dotenv()
        self.reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), 
                        client_secret=os.getenv('CLIENT_SECRET'), 
                        refresh_token=os.getenv('REFRESH_TOKEN'),
                        user_agent=os.getenv('USER_AGENT'))
        self.image_extensions = ('.jpg', '.jpeg', '.png')

    def get_submissions(self, sub_name, picture_mode, limit=15):
        reddit_submissions = []

        for submission in self.reddit.subreddit(sub_name).hot(limit=limit):
            if (picture_mode and self.is_valid_picture(submission)) or not picture_mode: 
                reddit_submissions.append(submission)
        
        return reddit_submissions

    def is_valid_picture(self, submission):
        return submission.url.endswith(self.image_extensions) and not submission.stickied

    def sub_exists(self, sub):
        try:
            self.reddit.subreddits.search_by_name(sub, exact=True)
        except NotFound:
            return False
        return True

    # todo: refactor
    def get_meme(self, sub_name=''):
        selected_sub = sub_name

        # random mode -> selects random subreddit from list
        if sub_name == '':
            sub_req = requests.get(os.getenv('SUBREDDIT_LIST')).text
            sub_list = sub_req.split('\n')
            selected_sub = random.choice(sub_list)

        # subreddit-specific mode -> selects random submission from given subreddit if subreddit name is provided
        reddit_submissions = self.get_submissions(sub_name=selected_sub, picture_mode=True)
        rand_submission = random.choice(reddit_submissions)

        return {
            'author': rand_submission.author,
            'title': rand_submission.title,
            'subreddit': rand_submission.subreddit_name_prefixed,
            'img': rand_submission.url
        }
    
    # todo: refactor
    def get_joke(self):
        reddit_submissions = self.get_submissions(sub_name='Jokes', picture_mode=False)
        rand_submission = random.choice(reddit_submissions)

        return {
            'author': rand_submission.author,
            'title': rand_submission.title,
            'text': rand_submission.selftext
        }