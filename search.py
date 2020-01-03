# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import praw
import requests
import random

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

    # todo: refactor
    def __get_submissions(self, subreddit_name, is_picture, limit=10):
        reddit_submissions = []

        def is_valid(url: str, is_picture: bool):
            if is_picture:
                return ('https://i.redd.it' in url)
            else:
                return True

        for submission in self.reddit.subreddit(subreddit_name).hot(limit=limit):
            if (is_valid(submission.url, is_picture) and not submission.stickied):
                reddit_submissions.append(submission)
        
        return reddit_submissions

    # todo: refactor
    def get_meme(self, subreddit_name=''):
        # random mode -> selects random subreddit from list
        if subreddit_name == '':
            subreddit_req = requests.get(os.getenv('SUBREDDIT_LIST')).text
            
            subreddit_list = subreddit_req.split('\n')
            
            reddit_submissions = self.__get_submissions(subreddit_name=subreddit_list[random.randint(0, len(subreddit_list) - 1)], is_picture=True)
        else:
            # subreddit-specific mode -> selects random submission from given subreddit
            reddit_submissions = self.__get_submissions(subreddit_name=subreddit_name, is_picture=True)

        rand_sub = reddit_submissions[random.randint(0, len(reddit_submissions) - 1)]

        return {
            'author': rand_sub.author,
            'title': rand_sub.title,
            'subreddit': rand_sub.subreddit_name_prefixed,
            'img': rand_sub.url
        }
    
    # todo: refactor
    def get_joke(self):
        reddit_submissions = self.__get_submissions(subreddit_name='Jokes', is_picture=False)

        rand_sub = reddit_submissions[random.randint(0, len(reddit_submissions) - 1)]

        return {
            'author': rand_sub.author,
            'title': rand_sub.title,
            'text': rand_sub.selftext
        }

def main():
    r = SearchReddit()
    print(r.get_meme())
    print('---')
    print(r.get_joke())

    # load_dotenv()
    # reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), 
    #             client_secret=os.getenv('CLIENT_SECRET'), 
    #             user_agent=os.getenv('USER_AGENT'), 
    #             username=os.getenv('USERNAME'), 
    #             password=os.getenv('PASSWORD'))

    # for submission in reddit.subreddit('comedyheaven').hot(limit=5):
    #     pprint(vars(submission))


if __name__ == '__main__':
    main()