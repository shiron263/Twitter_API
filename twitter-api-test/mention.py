#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, re
import pandas as pd
from auth import api

def get_mentions_names(tweet, mentions, count):
    if hasattr(tweet, "entities"):
                entities = tweet.entities
                if "user_mentions" in entities:
                    for ent in entities["user_mentions"]:
                        if ent is not None:
                            if "screen_name" in ent:
                                name = ent["screen_name"]
                                if name is not None:
                                    mentions.append(name)
                                    count = count + 1

def get_mentions_id(user_mentions):
    ids = []
    for username in user_mentions:
        user = api.get_user(screen_name=username)
        ids.append(user.id)
    return (ids)

def get_mentions_filter(user_mentions, keywords_list, count_mentions_keyword):
    count = 0
    check = 0
    ids = get_mentions_id(user_mentions)
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
                        count_mentions_keyword[index].append(word)
                        find = 1
                if find != 0:
                    break    # Break the loop to pass on the next user (to avoid miscalculation if the tag is present several time in the desc)
    for i in range(len(count_mentions_keyword)):
        print("\n" + str(keywords_list[i]) + " mentions = " + str(len(count_mentions_keyword[i]) - 1))
    return count_mentions_keyword