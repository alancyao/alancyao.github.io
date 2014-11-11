import random
import json
import praw

def get_im():
    user_agent = "abstinenceee chiyo scraper"
    r = praw.Reddit(user_agent=user_agent)
    s = [x.url for x in r.search("chiyo gekkan", "awwnime", limit=100) if x.url[-4] == '.']
    return random.choice(s)

