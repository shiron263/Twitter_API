#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, datetime, sys, json, time

consumerKey = '4Hs1cHal1n46fUAAt3FbtkTUh'
consumerSecret = 'alXV7bzdigd4Y6fmB2ZQT6svWGv2QEO7Jw1GPjDHhAxD9Qy9Ik'
accessToken = '761092062166917120-JTcJCIEBsNzAc1EGYmTD8zARkcxohOG'
accessTokenSecret = 'lbyMWLDEbTnd0ChnetHPLK59WzqP91Nqi9RaXXTPrAO83'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)