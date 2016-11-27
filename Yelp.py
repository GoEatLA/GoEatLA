from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


class YelpSearch:
    CONSUMER_KEY = "xr2AGjpXyVFSqOFZjukQjg"
    CONSUMER_SECRET = "LWKk-n_sXFJtpSxFvyNOK4yIChA"
    TOKEN = "mz6jzjOwwNiWHm9HM0SZL3lS2vAdFiv5"
    TOKEN_SECRET = "ffYjX0GfbQ7vrWnEjTPJFQiS93w"

    auth = Oauth1Authenticator(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                               token=TOKEN, token_secret=TOKEN_SECRET)
    client = Client(auth)


    def searchPlace(self,place):
        resp = self.client.search(place).businesses

        dicts_to_output = [
            {
                'name': biz.name,
                'id': biz.id,
                'rating': biz.rating,
                'review_count': biz.review_count,
                'location': biz.location,
            }
            for biz in resp
        ]

        print(dicts_to_output)
        return dicts_to_output