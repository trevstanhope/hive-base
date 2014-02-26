#!/usr/bin/env python
"""
HiveFeed
Developed by Trevor Stanhope
Mobile web-app Flask server for monitoring distributed hives hive monitors.
"""
# Constants
FLASK_IP = '0.0.0.0'
FLASK_PORT = 5000
FIREBASE = 'https://hivemind.firebaseio.com'

# Libraries
import json
from flask import Flask, url_for, render_template, request, redirect, session, flash
from flask_oauth import OAuth

# API Keys
with open('api_keys.json', 'r') as keyfile:
    keys = json.loads(keyfile.read())
    FIREBASE = keys['FIREBASE']
    FLASK_SECRET = keys['FLASK_SECRET']
    TWITTER_KEY = keys['TWITTER_KEY']
    TWITTER_SECRET = keys['TWITTER_SECRET']

# Global Objects
app = Flask(__name__)
app.secret_key = FLASK_SECRET
oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/', #API_V1.1
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    consumer_key=TWITTER_KEY,
    consumer_secret=TWITTER_SECRET
)

# Twitter Session
@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

# Index
@app.route('/')
def index():
    return render_template('index.html')

# Login 
@app.route('/login')
def login():
    if session.has_key('twitter_token'):
        del session['twitter_token']
    return twitter.authorize(callback=url_for('oauth_authorized',
        next=(request.args.get('next') or request.referrer or None)))

# OAuth
@app.route('/oauth_authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        return redirect(url_for('index')) #BADLOGIN
    else:
        session['twitter_token'] = (
            resp['oauth_token'],
            resp['oauth_token_secret']
        )
        session['twitter_user'] = resp['screen_name']
        return redirect(session['twitter_user'])

# User
@app.route('/<username>')
def user(username):

    resp = twitter.post('statuses/update.json', data={
        'status':'I just logged into HiveMind'
    })

    if resp.status == 403:
        print(str(resp.status) + ': Your tweet was too long.')
    elif resp.status == 401:
        print(str(resp.status) + ': Authorization error with Twitter.')
    elif resp.status == 410:
        print(str(resp.status) + ': Resource not found.')
    else:
        print(str(resp.status) + ': Other')

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

# Run Server
if __name__ == '__main__':
    app.run(FLASK_IP, port=FLASK_PORT, debug=True)

