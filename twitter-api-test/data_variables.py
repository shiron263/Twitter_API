#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, time, re


class MyData():
    username: str
    input_keyword: str
    in_start: str
    list_start: str
    in_end: str
    list_end: str
    list_keywords: list
    startDate: datetime.datetime
    endDate:  datetime.datetime

class MyResults():
    statues_info = list
    count_tweet = int
    count_mentions = int
    count_mentions_keyword = list
    count_followers_keyword = list
    count_tweets_keyword = list
    count_likes = int
    count_rt = int
    engagement = int

# Initialization of data variables
my_input = MyData()
my_input.username = input("Twitter username: ").lower()       # Get the username in input (transform into lowercase)
my_input.input_keyword = input("Tags: ").lower()              # Get tags in input (transform into lowercase)
my_input.in_start = input("Start date (AAAA/MM/DD): ")
my_input.in_end = input("End date (AAAA/MM/DD): ")
my_input.list_start = re.findall(r"[^\W\d_]+|\d+", my_input.in_start)
my_input.list_end = re.findall(r"[^\W\d_]+|\d+", my_input.in_end)
my_input.list_keywords = re.findall(r"[^\W\d_]+|\d+", my_input.input_keyword)    # Split every non-alphanum characters("-nucléaire& > nucléaire")
my_input.startDate = datetime.datetime(int(my_input.list_start[0]),
                                    int(my_input.list_start[1]), int(my_input.list_start[2]), 0, 0, 0)            # Temporaires
my_input.endDate = datetime.datetime(int(my_input.list_end[0]),
                                    int(my_input.list_end[1]), int(my_input.list_end[2]), 0, 0, 0)                # Temporaires

my_result = MyResults()
my_result.count_tweet = 0
my_result.count_mentions = 0
my_result.count_likes = 0
my_result.count_rt = 0
count_tweet_tag = 0
engagement = 0
my_result.count_mentions_keyword = [[0 for i in range(1)] for j in range(len(my_input.list_keywords))]
my_result.count_followers_keyword = [[0 for i in range(1)] for j in range(len(my_input.list_keywords))]
my_result.statues_info = []