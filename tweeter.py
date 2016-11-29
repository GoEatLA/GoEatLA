#! /usr/bin/python

import tweepy
import ast

CONSUMER_KEY = "XqNwYplxMeHiDEl2iSNhKVB7J"
CONSUMER_SECRET = "a4rtEW9M7E0AuxeGmpfisDf4aTrjUPhgT1yyGFVBnGgTFoJDXy"
ACCESS_KEY  = "796494214154649600-OjrAVh8SweH7aagpO48cnJmLksOhEg4"
ACCESS_SECRET = "lTvNGcqdhgar7xEdYFb7Nzvufg9iaUjdCNClegJFnh59P"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def get_previous():
	with open("previous.txt", "r") as f:
		a = f.readline()

	print(a)
	previous = ast.literal_eval(a)
	return previous

def set_previous(aList):
	f = open("previous.txt", "w")
	f.write(str(aList))
	f.close()


def updateMsg(tweet):
	api.update_status(tweet)

def get_mentions():
	tweets = []

	with open("last_id.txt", "r") as f:
		last_id = f.readline()

	newTweets = api.mentions_timeline(since_id = last_id)
	for a in newTweets:
		last_id = str(a.id)
		f = open("last_id.txt", "w")
		f.close()
		f = open("last_id.txt", "w")
		f.write(last_id)
		f.close()
		tweets.append((a.user.screen_name, a.text[9:]))

	set_previous(tweets)
	return tweets