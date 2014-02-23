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

# Index
@app.route('/')
def index():
    return render_template('index.html')

# User
@app.route('/<username>')
def user(username):
    return render_template('user.html',
        username=username
    )

# Aggregator
@app.route('/<username>/<aggregator>')
def aggregator(username, aggregator):
    return render_template('aggregator.html',
	    aggregator=aggregator,
	    username=username
    )

# Graph
@app.route('/<username>/<aggregator>/<graph>')
def graph(username, aggregator, graph):
    return render_template('graph.html',
	    aggregator=aggregator,
	    username=username,
        graph=graph
    )

# 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# Main
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

