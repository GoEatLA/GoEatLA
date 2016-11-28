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

		t = threading.Thread(target = self.run)
		t.daemon = True
		t.start()

	def goo_shorten_url(address):
		post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAMjzI6DES-ntXZk-cC448DMDE3tnxaUiQ'
		longurl = 'http://www.google.com/maps/dir/Current+Location/' + address
		payload = {'longUrl' : longurl}
		headers = {'content-type' : 'application/json'}
		r = requests.post(post_url, data=json.dumps(payload), headers=headers)
		return r.json()['id']

	def run(self):
		"""Continuously post on twitter"""
		while True:
			places = self.yelp.searchPlace("Los Angeles")
			rng = random.randint(0,len(places) - 1)
			location = map(lambda x: x.encode('ascii'), places[rng]['location'])
			address = ' '.join(location)
			name = places[rng]['name']
			googlelink = self.goo_shorten_url(address)
			tweeter.updateMsg(name + " at " + googlelink)
			#Send 'address' info to google api
			time.sleep(self.minutes)


goEatLA = GoEatLA(Yelp.YelpSearch(),30)
