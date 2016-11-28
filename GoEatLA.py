#! /usr/bin/python3

import threading
import time
import Yelp
import tweeter
import random


class GoEatLA:
	
	def __init__(self, yelp, minutes = 3):
	#def __init__(self, minutes = 3):
		self.yelp = yelp
		self.minutes = minutes #* 60

		t = threading.Thread(target = self.run)
		t.daemon = True
		t.start()


	def run(self):
		"""Continuously post on twitter"""
		while True:
			places = self.yelp.searchPlace("Los Angeles")
			rng = random.randint(0,len(places) - 1)
			location = map(lambda x: x.encode('ascii'), places[rng]['location'])
			address = ' '.join(location)
			name = places[rng]['name']
			tweeter.updateMsg(name + " at " + address)
			#Send 'address' info to google api
			time.sleep(self.minutes)


goEatLA = GoEatLA(Yelp.YelpSearch(),30)
