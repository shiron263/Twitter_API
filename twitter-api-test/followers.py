#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, re
import pandas as pd
from auth import api
from user import user_followers_ids

def follower_filter(username, keywords_list, count_followers_keyword):
    """
    This function give us the filtered followers number
    """
    count = 0
    check = 0
    ids = user_followers_ids(username)
    while(check < len(ids)):
        hundred_ids=[[0 for i in range(1)] for j in range(100)]   # Put 100 ids in this list because api.lookup_user function can't handle more than 100 ids in the same time
        for i in range(100):
            if check < len(ids):
                hundred_ids[i] = ids[check]
                check += 1
        test = api.lookup_users(user_ids=hundred_ids)
        for user in test:
            find = 0
            description = str(user.description)
            desc_split = re.findall(r"[^\W\d_]+|\d+", description)  # Split every non-alphanum characters("-nucléaire& > nucléaire")
            for word in desc_split:
                index = -1
                for keyword in keywords_list:
                    index += 1
                    if word.lower() == keyword:
                        count_followers_keyword[index].append(word)
                        find = 1
                if find != 0:
                    break    # Break the loop to pass on the next user (to avoid miscalculation if the tag is present several time in the desc)
    for i in range(len(count_followers_keyword)):
        print(str(keywords_list[i]) + " followers = " + str(len(count_followers_keyword[i]) - 1))
    return count_followers_keyword