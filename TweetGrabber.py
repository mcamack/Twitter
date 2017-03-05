import sys
import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from access_tokens import *


def process_or_store(tweet):
	print(json.dumps(tweet))

class MyListener(StreamListener):
	def on_data(self, data):
		try:
			#with open('tweets.json', 'a') as f:
			fname = sys.argv[1]
			with open(fname, 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print(status)
		return True

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
twitter_stream = Stream(auth, MyListener())
search_term = sys.argv[2]
twitter_stream.filter(track=[search_term])



#for status in tweepy.Cursor(api.home_timeline).items(1):
	#print(status.text)

#for friend in tweepy.Cursor(api.friends).items():
	#process_or_store(friend._json)
	#print(friend.name)