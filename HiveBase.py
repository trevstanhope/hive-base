#!/usr/bin/env python
"""
HiveMind-Plus Server
Developed by Trevor Stanhope
"""

# Libraries
from flask import Flask, url_for, render_template, request, redirect, session
from firebase import firebase, jsonutil
from flask_oauth import OAuth

# Global Objects
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
base = firebase.FirebaseApplication('https://hivemind-plus.firebaseio.com', None)
oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    consumer_key='7x3M6ZT9dbO6pr1zeiutg',
    consumer_secret='534Mkp7RJZ5asaC9iURV6hGa89gQhQXUDuPo9Ing'
)

# Getter
@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

# Login
@app.route('/login')
def login():
    return twitter.authorize(callback=url_for('oauth_authorized',
        next=(request.args.get('next') or request.referrer or None)))

# OAuth
@app.route('/oauth_authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        return redirect(next_url)
    else:
        session['twitter_token'] = (
            resp['oauth_token'],
            resp['oauth_token_secret']
        )
        session['twitter_user'] = resp['screen_name']
        return redirect(next_url)

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


