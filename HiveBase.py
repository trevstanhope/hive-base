#!/usr/bin/env python
"""
HiveBase
Developed by Trevor Stanhope
MongoDB + SKLearn hub for aggregated data
"""
# Libraries
import json, pymongo, datetime
from pymongo import MongoClient
from firebase import firebase

# Constants
MONGO_IP = '127.0.0.1'
MONGO_PORT = 27017
FIREBASE = 'https://hivemind.firebaseio.com'

# API Keys
with open('api_keys.json', 'r') as keyfile:
    keys = json.loads(keyfile.read())
    FIREBASE = keys['FIREBASE']
    # FLASK_SECRET = os.getenv(keys['FLASK_SECRET'])
    TWITTER_KEY = keys['TWITTER_KEY']
    TWITTER_SECRET = keys['TWITTER_SECRET']

# HiveBase Class
class HiveBase:

    ## Initialize
    def __init__(self):
        self.mongo = MongoClient()
        self.mongo = MongoClient(MONGO_IP, MONGO_PORT)  
        self.base = firebase.FirebaseApplication(FIREBASE, None) #UNUSED  

    ##
    def listen(self):
        print(str(self.base))
        return True
    
    ## Add to database
    def add_to(post, db_name, collection_name):
        db = self.mongo[db_name]
        collection = db[collection_name]
        post_id = collection.insert(post)
        return post_id

    ## run
    def run(self):
        while True:
            try:
                self.listen()
            except Exception as error:
                print(str(error))

if __name__ == '__main__':
    base = HiveBase()
    base.run()
