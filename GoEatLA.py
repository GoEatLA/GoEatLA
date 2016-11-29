#! /usr/bin/python3

import threading
import datetime
import Yelp
import tweeter
import random
import requests
import json

class GoEatLA:

	counter = 0
	
	def __init__(self, yelp, posttime = 30, readtime = 30):
		self.yelp = yelp
		self.posttime = posttime
		self.readtime = readtime
		self.subarea = ['Antelope Valley', 'Agoura Hills', 'Alhambra', 'Arcadia', 'Baldwin Park',
		'Beverly Hills', 'Boyle Heights', 'Burbank', 'Calabasas', 'Cerritos', 'Claremont', 'Compton', 'Culver City', 
		'Downtown, Los Angeles', 'El Monte', 'Hacienda Heights', 'Griffith Park', 'Koreatown', 'Inglewood', 'Lancaster', 'Malibu', 'Marina del Rey',
		'North Hollywood', 'Pasadena', 'Pomona', 'Redondo Beach', 'Rowland Heights', 'Santa Monica', 'Studio City', 'Torrance',
		'Van Nuys', 'Venice', 'West Hollywood', 'West Covina', 'Westlake']

	def makeTweets(self):
		places = self.yelp.searchStuff(random.choice(self.subarea))
		rng = random.randint(0, len(places) - 1)
		address = ' '.join(places[rng]['location'])
		name = places[rng]['name']
		googlelink = self.goo_shorten_url(address)
		tweeter.updateMsg(name + " at " + googlelink)
		threading.Timer(self.posttime, self.makeTweets).start()

	def getTweets(self):

		prev = tweeter.get_previous()
		otherTweets = tweeter.get_mentions()
		if len(prev) != 0:
			simplifiedTweets = list(set(otherTweets) - set(prev))
		else:
			simplifiedTweets = otherTweets[:]

		print("New Tweets:", simplifiedTweets, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

		for person in simplifiedTweets:
			places = self.yelp.searchStuff(random.choice(self.subarea), person[1])
			rng = random.randint(0, len(places) - 1)
			address = ' '.join(places[rng]['location'])
			name = places[rng]['name']
			googlelink = self.goo_shorten_url(address)
			replyTo = "@%s"% person[0]
			try:
				tweeter.updateMsg(replyTo + " #" + str(self.counter) + " " + name + " at " + googlelink)
				self.counter += 1
			except tweeter.error.TweepyError as err:
				print (err)

		threading.Timer(self.readtime, self.getTweets).start()

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
		self.getTweets()

goEatLA = GoEatLA(Yelp.YelpSearch(),45)
goEatLA.run()