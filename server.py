#!/usr/bin/env python
"""
HiveMind-Plus Server
Developed by Trevor Stanhope
"""

# Libraries
from flask import Flask, url_for, render_template
from firebase import firebase, jsonutil

# Global Objects
app = Flask(__name__)
base = firebase.FirebaseApplication('https://hivemind-plus.firebaseio.com', None)

# Flask Functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/<username>/<aggregator>')
def aggregator(username, aggregator):
    return render_template('aggregator.html', aggregator=aggregator, username=username)

@app.route('/<username>/<aggregator>/internal_temp')
def internal_temp(username, aggregator):
    return render_template('internal_temp.html', aggregator=aggregator, username=username)

@app.route('/<username>/<aggregator>/external_temp')
def external_temp(username, aggregator):
    return render_template('external_temp.html', aggregator=aggregator, username=username)

@app.route('/<username>/<aggregator>/internal_humidity')
def internal_humidity(username, aggregator):
    return render_template('internal_humidity.html', aggregator=aggregator, username=username)

@app.route('/<username>/<aggregator>/external_humidity')
def external_humidity(username, aggregator):
    return render_template('external_humidity.html', aggregator=aggregator, username=username)

@app.route('/<username>/<aggregator>/frequency')
def frequency(username, aggregator):
    return render_template('frequency.html', aggregator=aggregator, username=username)

@app.route('/<username>/<aggregator>/amplitude')
def amplitude(username, aggregator):
    return render_template('amplitude.html', aggregator=aggregator, username=username)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# Main
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


