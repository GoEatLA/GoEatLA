from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

CONSUMER_KEY = "xr2AGjpXyVFSqOFZjukQjg"
CONSUMER_SECRET = "LWKk-n_sXFJtpSxFvyNOK4yIChA"
TOKEN = "mz6jzjOwwNiWHm9HM0SZL3lS2vAdFiv5"
TOKEN_SECRET = "ffYjX0GfbQ7vrWnEjTPJFQiS93w"


auth = Oauth1Authenticator(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                           token=TOKEN, token_secret=TOKEN_SECRET)
client = Client(auth)

resp = client.search("Los Angeles")
for business in resp:
    print(business)
