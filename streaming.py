from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.utils import import_simplejson

from pymongo import MongoClient

mongoc = MongoClient()
db = mongoc.natweet
col = db.tweets
json = import_simplejson()

#Atlanta bounding box including Cobb & Acworth
loc = [-84.730682,33.502469,-83.94104,34.114079]

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

class TwitterStreamListener(StreamListener):
	#input host = here
	mongoc = MongoClient(host = 'localhost')
	db = mongoc.natweet
	col = db.tweets
	json = import_simplejson()

	def on_data(self, data):
		if data[0].isdigit():
			pass
		else:
			col.insert(json.loads(data))
			print(json.loads(data))

	def on_error(self, status):
		return False

l = TwitterStreamListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(locations = loc)
