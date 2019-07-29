#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from auth import api

def user_info(username):
    user = api.get_user(username)
    client_id = user.id
    client_description = user.description
    client_followers = user.followers_count


def user_followers_ids(username):
    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=username).pages():
        ids.extend(page)
    return (ids)