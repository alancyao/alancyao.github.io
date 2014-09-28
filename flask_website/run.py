#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    default = "https://files.yande.re/image/397343eeb60a293f0d645e4ff337cb90/yande.re%20298826%20gekkan_shoujo_nozaki-kun%20nozaki_umetarou%20sakura_chiyo%20seifuku%20thighhighs.jpg"
    return render_template('index.html', imurl=default)

if __name__ == '__main__':
    app.run(debug=True)
