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
	tweets = []

	with open("last_id.txt", "r") as f:
		last_id = f.readline()

	for a in api.mentions_timeline(since_id = last_id):
		last_id = str(a.id)
		f = open("last_id.txt", "w")
		f.close()
		f = open("last_id.txt", "w")
		f.write(last_id)
		f.close()
		tweets.append((a.user.screen_name, a.text[9:]))
	return tweets