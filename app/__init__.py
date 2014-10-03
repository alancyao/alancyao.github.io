#!/usr/bin/env python
from flask import Flask, redirect
app = Flask(__name__)

from flask import render_template
import helpers

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return app.send_static_file('files/resume.pdf')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cs184')
def cs184():
    return redirect("https://hkn.eecs.berkeley.edu/~alanyao/CS184/index.html", code=302)

@app.route('/sakurachiyo')
def sakurachiyo():
    im = helpers.get_im()
    return render_template('sakurachiyo.html', imurl=im)
