import oauth2 as oauth
import json, random, sys, inspect

def get_tweet_about(keyword):
	search_url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + keyword
	client = get_authenticated_client()
	response, data = client.request(search_url)
	tweets = json.loads(data)
	result = random.choice(tweets['statuses'])
	return result

def get_authenticated_client():
	consumer_key = "<get your own>"
	consumer_secret = "<shhh it's a secret>"
	consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
	request_token_url = "https://api.twitter.com/oauth/request_token"
	client = oauth.Client(consumer)
	return client

try:
    keyword = sys.argv[1]
    tweet = get_tweet_about(keyword)
    print tweet['text']
    print "\tauthor: " + tweet['user']['screen_name']
    print "\tsource: https://twitter.com/" + tweet['user']['screen_name'] + "/status/" + tweet['id_str']
except:
    print "You must pass in a keyword like"
    print "\tpython " + inspect.getfile(inspect.currentframe()) + " <keyword>"
    pass

