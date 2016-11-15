#! /usr/bin/python

import tweepy

CONSUMER_KEY = "XqNwYplxMeHiDEl2iSNhKVB7J"
CONSUMER_SECRET = "a4rtEW9M7E0AuxeGmpfisDf4aTrjUPhgT1yyGFVBnGgTFoJDXy"
ACCESS_KEY  = "796494214154649600-OjrAVh8SweH7aagpO48cnJmLksOhEg4"
ACCESS_SECRET = "lTvNGcqdhgar7xEdYFb7Nzvufg9iaUjdCNClegJFnh59P"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("IMA BOT BITCH")