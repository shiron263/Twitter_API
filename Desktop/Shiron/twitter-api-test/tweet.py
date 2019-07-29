#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, re
import pandas as pd
from auth import api
from mention import get_mentions_names, get_mentions_filter

def get_statues(my_input_data, my_result_data, tweets, user_mentions, tmpTweets):
    for tweet in tmpTweets:
        if tweet.created_at < my_input_data.endDate and tweet.created_at > my_input_data.startDate:
            get_mentions_names(tweet, user_mentions, my_result_data.count_mentions)
            tweets.append(tweet)
            my_result_data.count_tweet = my_result_data.count_tweet + 1
    while (tmpTweets[-1].created_at > my_input_data.startDate):
        tmpTweets = api.user_timeline(my_input_data.username, max_id = tmpTweets[-1].id)
        for tweet in tmpTweets:
            if tweet.created_at < my_input_data.endDate and tweet.created_at > my_input_data.startDate:
                get_mentions_names(tweet, user_mentions, my_result_data.count_mentions)
                tweets.append(tweet)
                my_result_data.count_tweet = my_result_data.count_tweet + 1

def month_tweet(my_input_data, my_result_data):
    tweets = []
    user_mentions = []
    tmpTweets = api.user_timeline(my_input_data.username)
    get_statues(my_input_data, my_result_data, tweets, user_mentions, tmpTweets)
    count_mentions_filter = get_mentions_filter(user_mentions, my_input_data.list_keywords, my_result_data.count_mentions_keyword)
    user_locs = [[tweet.user.id, tweet.text, tweet.created_at] for tweet in tweets]
    tweet_info = pd.DataFrame(data=user_locs, columns=['user', 'text', 'date'])
    print("\ntweet month = " + str(my_result_data.count_tweet))
    return tweet_info

def filter_tweet(my_input_data, my_result_data):
    count = 0
    tweets_info = month_tweet(my_input_data, my_result_data)
    tweets = tweets_info['text']
    for tweet in tweets:
        find = 0
        parsing_tweet = re.findall(r"[^\W\d_]+|\d+", tweet)  # Split every non-alphanum characters("-nucléaire& > nucléaire")
        for word in parsing_tweet:
            index = -1
            for keyword in my_input_data.list_keywords:
                index += 1
                if word.lower() == keyword:
                    count = count + 1
                    find = 1
            if find != 0:
                break    # Break the loop to pass on the next user (to avoid miscalculation if the tag is present several time in the desc)
    for i in range(len(my_input_data.list_keywords)):
        print("\n" + str(my_input_data.list_keywords[i]) + " tweets = " + str(count))
    return count