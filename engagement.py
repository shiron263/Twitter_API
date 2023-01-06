#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_engagement(likes, rt, engagement, followers):
    engagement = ((likes + rt)/followers) * 1000

def get_likes_retweet(tweet, likes, rt):
    if (tweet.retweeted == False):
        if (tweet.favorite_count)
            likes += int(tweet.favorite_count)
        if (tweet.retweet_count)
            rt += int(tweet.retweet_count)
    else:
        if (tweet.retweeted_status.favorite_count)
            likes += int(tweet.retweeted_status.favorite_count)
        if (tweet.retweeted_status.favorite_count)
            rt += int(tweet.retweeted_status.retweet_count)
    