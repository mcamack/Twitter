import sys
import operator
import json
from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
pos_score = 0
neg_score = 0

fname = sys.argv[1]

with open(fname, 'r') as f:
	count_all = Counter()
	for line in f:
		tweet = json.loads(line).get('text')

		#filter out nulls
		if(tweet is not None):
			#get sentiment score for tweet
			score = sia.polarity_scores(tweet)

			#store most positive tweet
			if(score['pos'] > pos_score):
				pos_score = score['pos']
				pos = {'score':pos_score, 'tweet':tweet}

			#store most negative tweet
			if(score['neg'] > neg_score):
				neg_score = score['neg']
				neg = {'score':neg_score, 'tweet':tweet}

			#store a count of most common terms
			words = tweet.split()
			terms_all = [term for term in words if len(term)>4]
			count_all.update(terms_all)

#Print Results of most common terms, most positive and negative tweets
print('Most used terms:')
print(nltk.FreqDist(terms_all).keys())

print('\nMost positive tweet is: ' + str(pos['score']))
print(pos['tweet'])

print('\nMost negative tweet is: ' + str(neg['score']))
print(neg['tweet'])