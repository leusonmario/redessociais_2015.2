import tweepy
import json
import xlwt
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'HOXQGnZkXlunsvLByKPpmNG6b'
consumer_secret = 'yxkfVWR2JZ2neXk4y9FYJZb3EFjPNycIauEsfhvB8vtqUemDxX'
access_token = '326313390-wnvmRZeLGBg4gsnEX2XNLgT6RNTqMrK4EIXybAKu'
access_token_secret = '0zaN1el46tWJTAGeD7MYxPMmdZkPTT5EdYUUSYQZtqWe3'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# planilha xls
workbook = xlwt.Workbook();
worksheet = workbook.add_sheet(u'Tweets')


api = tweepy.API(auth)
q = '#dilma'
count = 10
search_results = api.search(q=q, count=count)

iteradorTweets = 0

for tweet in search_results:
	#print (tweet.text.encode("utf-8"))
	worksheet.write(iteradorTweets,0,tweet.created_at)
	worksheet.write(iteradorTweets,1,tweet.id)
	worksheet.write(iteradorTweets,2,tweet.user.screen_name)
	worksheet.write(iteradorTweets,3,tweet.text)
	iteradorTweets+=1

workbook.save('tweets.xls')