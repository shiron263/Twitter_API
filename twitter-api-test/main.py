#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data_variables import my_input, my_result
from user import user_info
from followers import follower_filter
from tweet import filter_tweet, month_tweet
from auth import api


if __name__ == '__main__':
    # follower_filter(my_input.username, my_input.list_keywords, my_result.count_followers_keyword) #Get filtered follwers
    # filter_tweet(my_input, my_result) # Get tweet month, mentions filtered, tweet filtered
    print("startDate: ", my_input.list_start)
    print("endDate: ", my_input.list_end)