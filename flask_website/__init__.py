#!/usr/bin/env python
from flask import Flask
from flask import render_template
import random
import json
import praw
app = Flask(__name__)

def get_im():
    user_agent = "abstinenceee chiyo scraper"
    r = praw.Reddit(user_agent=user_agent)
    s = [x.url for x in r.search("chiyo gekkan", "awwnime", limit=100) if x.url[-4] == '.']
    return random.choice(s)

@app.route('/')
def index():
    im = get_im()
    return render_template('index.html', imurl=im)

if __name__ == '__main__':
    app.run(debug=True)
