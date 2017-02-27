import sys
import operator
import json
from collections import Counter
import nltk

#fname = 'tweets.json'
fname = sys.argv[1]

with open(fname, 'r') as f:
	count_all = Counter()
	for line in f:
		tweet = json.loads(line)

		tweet = tweet.get('text')
		if(tweet is not None):
			#print(tweet)
			words = tweet.split()
			#print(words)

			terms_all = [term for term in words if len(term)>4]
			count_all.update(terms_all)
			#print(count_all.most_common(10))

print(nltk.FreqDist(terms_all).keys())