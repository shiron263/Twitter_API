#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, re
import pandas as pd
from auth import api
from mention import get_mentions_names, get_mentions_filter

def get_statues(my_input, my_result, tweets, user_mentions, tmpTweets):
    for tweet in tmpTweets:
        if tweet.created_at < my_input.endDate and tweet.created_at > my_input.startDate:
            get_mentions_names(tweet, user_mentions, my_result.count_mentions)
            tweets.append(tweet)
            my_result.count_tweet = my_result.count_tweet + 1
    while (tmpTweets[-1].created_at > my_input.startDate):
        tmpTweets = api.user_timeline(my_input.username, max_id = tmpTweets[-1].id)
        for tweet in tmpTweets:
            if tweet.created_at < my_input.endDate and tweet.created_at > my_input.startDate:
                get_mentions_names(tweet, user_mentions, my_result.count_mentions)
                tweets.append(tweet)
                my_result.count_tweet = my_result.count_tweet + 1

def month_tweet(my_input, my_result):
    tweets = []
    user_mentions = []
    tmpTweets = api.user_timeline(my_input.username)
    get_statues(my_input, my_result, tweets, user_mentions, tmpTweets)
    count_mentions_filter = get_mentions_filter(user_mentions,
                                                my_input.list_keywords, my_result.count_mentions_keyword)
    user_locs = [[tweet.user.id, tweet.text, tweet.created_at] for tweet in tweets]
    tweet_info = pd.DataFrame(data=user_locs, columns=['user', 'text', 'date'])
    return tweet_info

def filter_tweet(my_input, my_result):
    count = 0
    tweets_info = month_tweet(my_input, my_result)
    tweets = tweets_info['text']
    for tweet in tweets:
        find = 0
        parsing_tweet = re.findall(r"[^\W\d_]+|\d+", tweet)  # Split every non-alphanum characters("-nucléaire& > nucléaire")
        for word in parsing_tweet:
            index = -1
            for keyword in my_input.list_keywords:
                index += 1
                if word.lower() == keyword:
                    count = count + 1
                    find = 1
            if find != 0:
                break    # Break the loop to pass on the next user (to avoid miscalculation if the tag is present several time in the desc)
    for i in range(len(my_input.list_keywords)):
        print(str(my_input.list_keywords[i]) + " tweets = " + str(count))
    return count