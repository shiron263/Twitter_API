#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, datetime, sys, json, time

consumerKey = ''
consumerSecret = ''
accessToken = ''
accessTokenSecret = ''
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)