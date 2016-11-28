#! /usr/bin/python3

import threading
import time
import Yelp
import tweeter
import random
import requests
import json

class GoEatLA:
	
	def __init__(self, yelp, minutes = 3):
	#def __init__(self, minutes = 3):
		self.yelp = yelp
		self.minutes = minutes #* 60

	def makeTweets(self):
		places = self.yelp.searchPlace("Los Angeles")
		rng = random.randint(0, len(places) - 1)

		# Python 2 only
		# location = map(lambda x: x.encode('ascii'), places[rng]['location'])
		# address = ' '.join(location)

		address = ' '.join(places[rng]['location'])
		name = places[rng]['name']
		googlelink = self.goo_shorten_url(address)
		tweeter.updateMsg(name + " at " + googlelink)
		threading.Timer(self.minutes, self.makeTweets).start()

	def getTweets(self):
		otherTweets = tweeter.get_mentions()
		print(otherTweets)

		places = self.yelp.searchStuff("Los Angeles", otherTweets[0][1])

		#not working paramter search I think
		print(places[0]['name'])


	def goo_shorten_url(self, address):
		post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAMjzI6DES-ntXZk-cC448DMDE3tnxaUiQ'
		longurl = 'http://www.google.com/maps/dir/Current+Location/' + address
		payload = {'longUrl' : longurl}
		headers = {'content-type' : 'application/json'}
		r = requests.post(post_url, data=json.dumps(payload), headers=headers)
		return r.json()['id']

	def run(self):
		"""Continuously post on twitter and wait for response"""
		#self.makeTweets()
		self.getTweets()

goEatLA = GoEatLA(Yelp.YelpSearch(),30)
goEatLA.run()
