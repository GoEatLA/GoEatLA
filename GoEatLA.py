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
		self.subarea = ['Antelope Valley', 'Agoura Hills', 'Alhambra', 'Arcadia', 'Baldwin Park',
		'Beverly Hills', 'Boyle Heights', 'Burbank', 'Calabasas', 'Cerritos', 'Claremont', 'Compton', 'Culver City', 
		'Downtown, Los Angeles', 'El Monte', 'Hacienda Heights', 'Griffith Park', 'Koreatown', 'Inglewood', 'Lancaster', 'Malibu', 'Marina del Rey',
		'North Hollywood', 'Pasadena', 'Pomona', 'Redondo Beach', 'Rowland Heights', 'Santa Monica', 'Studio City', 'Torrance',
		'Van Nuys', 'Venice', 'West Hollywood', 'West Covina', 'Westlake']

	def makeTweets(self):
		places = self.yelp.searchPlace(random.choice(self.subarea))
		rng = random.randint(0, len(places) - 1)

		# Python 2 only
		# location = map(lambda x: x.encode('ascii'), places[rng]['location'])
		# address = ' '.join(location)

		address = ' '.join(places[rng]['location'])
		name = places[rng]['name']
		googlelink = self.goo_shorten_url(address)
		tweeter.updateMsg(name + " at " + googlelink)
		threading.Timer(self.minutes, self.makeTweets).start()


	def goo_shorten_url(self, address):
		post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAMjzI6DES-ntXZk-cC448DMDE3tnxaUiQ'
		longurl = 'http://www.google.com/maps/dir//' + address
		payload = {'longUrl' : longurl}
		headers = {'content-type' : 'application/json'}
		r = requests.post(post_url, data=json.dumps(payload), headers=headers)
		return r.json()['id']

	def run(self):
		"""Continuously post on twitter and wait for response"""
		self.makeTweets()

goEatLA = GoEatLA(Yelp.YelpSearch(),30)
goEatLA.run()
