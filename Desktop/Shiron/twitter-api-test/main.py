#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, datetime, sys, json, time, re
import pandas as pd
from user import user_info
from followers import follower_filter
from tweet import filter_tweet, month_tweet
from auth import api


class MyData():
    username: str
    input_keyword: str
    list_keywords: list
    startDate: datetime.datetime
    endDate:  datetime.datetime

class MyResults():
    statues_info = list
    count_tweet = int
    count_mentions = int
    count_mentions_keyword = list
    count_followers_keyword = list

# Initialization of data variables
my_input_data = MyData()
my_input_data.username = input("Twitter username: ").lower()           # Get the username in input (transform into lowercase)
my_input_data.input_keyword = input("Tags: ").lower()                   # Get tags in input (transform into lowercase)
my_input_data.list_keywords = re.findall(r"[^\W\d_]+|\d+", my_input_data.input_keyword)    # Split every non-alphanum characters("-nucléaire& > nucléaire")
my_input_data.startDate = datetime.datetime(2019, 7, 1, 0, 0, 0)        # Temporaires
my_input_data.endDate = datetime.datetime(2019, 7, 31, 0, 0, 0)         # Temporaires

my_result_data = MyResults()
my_result_data.count_tweet = 0
my_result_data.count_mentions = 0
my_result_data.count_mentions_keyword = [[0 for i in range(1)] for j in range(len(my_input_data.list_keywords))]
my_result_data.count_followers_keyword = [[0 for i in range(1)] for j in range(len(my_input_data.list_keywords))]
my_result_data.statues_info = []


if __name__ == '__main__':
    follower_filter(my_input_data.username, my_input_data.list_keywords, my_result_data.count_followers_keyword) #Get filtered follwers
    filter_tweet(my_input_data, my_result_data) # Get tweet month, mentions filtered, tweet filtered
