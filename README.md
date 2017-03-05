# Twitter

Project to mine Twitter data and perform sentiment analysis. There are 2 files:
## TweetGrabber.py <output_file> <Twitter_search_string>
* This uses the tweepy package to open a Twitter listening stream and saves all tweets in json format to the output file

## jsonParser.py <input_file>
* This uses the Natural Language Toolkit (NLTK) and parses through the saved json tweets, outputting the most popular "phrases" with greater than 4 characters. Phrases includes words, hashtags, links, @mentions and the script also saves retweets as individual tweets. In a way this is good, as it shows what is being "liked" or discussed more often and increments the counts of those words.
* It then uses the NLTK to perform sentiment analysis on each individual tweet, saving the most positive and negative tweets. It then outputs these values and a list of the most common phrases.

## access_tokens.py
* This file contains access tokens for me to access Twitter. Added to the .gitignore file so this doesn't actually show up on public GitHub

# Results
In about 10 minutes, TweetGrabber.py saved 3692 tweets (22.8MB) when the search string was "Trump" ... it was about 5PM Pacific Time and I got a lot more tweets than when I did this closer to 11PM.  

jsonParser crunched the data and the results were stored in a Dictionary. The keys were:  
White  
https://t.co/WrqNRD...  
Trump  
https://t.co/Z69wgwywiC  
media  
Social  
House  
replace  
suggests  
Baldwin  
Dinner  
@THR  
Correspondents  
  
Most positive tweet is: 0.733  
Keep hope alive. https://t.co/huOJ8nwf6c  
  
Most negative tweet is: 0.853  
Frightening gullibility. https://t.co/aW5eH8qomH  
  
Overall, I found it pretty funny and accurate to what was in the news right when I did this. Trump was going to boycott the White House Correspondents Dinner and people wanted Alec Baldwin to replace him. The sentiment analysis portion was also pretty accurate, although it does not sense sarcasm nor know what the links are referring to.
