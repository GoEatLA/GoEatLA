#! /usr/bin/python

import tweepy

CONSUMER_KEY = "XqNwYplxMeHiDEl2iSNhKVB7J"
CONSUMER_SECRET = "a4rtEW9M7E0AuxeGmpfisDf4aTrjUPhgT1yyGFVBnGgTFoJDXy"
ACCESS_KEY  = "796494214154649600-OjrAVh8SweH7aagpO48cnJmLksOhEg4"
ACCESS_SECRET = "lTvNGcqdhgar7xEdYFb7Nzvufg9iaUjdCNClegJFnh59P"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def updateMsg(tweet):
	api.update_status(tweet)

def get_mentions():
	#return api.mentions_timeline()[0].text
	tweets = []
	for a in api.mentions_timeline():
		tweets.append((a.user.screen_name, a.text[9:]))
	return tweets