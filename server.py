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

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

# Main
if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
