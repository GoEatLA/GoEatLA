#! /usr/bin/python3

import threading
import time
import Yelp
import tweeter


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
		# while True:
		# 	print(yelp.searchPlace("Los Angeles"))
		# 	tweeter.updateMsg("Hello Testing!")
		# 	time.sleep(self.minutes)
		print(yelp.searchPlace("Los Angeles"))
		tweeter.updateMsg("Hello Testing!")
		time.sleep(self.minutes)


yelp = Yelp.YelpSearch()

goEatLA = GoEatLA(yelp,30)
