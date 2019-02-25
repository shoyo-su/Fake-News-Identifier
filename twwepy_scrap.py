
keyword=input("Mention the keyword:")


import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
consumer_key='KDTcZfPqPwk3oCnN86ahvVDtN'
consumer_secret='npTOrTp6fO7v9roLoZEdbyMIMjF7H0yC3HVL3oK7P3bPj1QXri'
access_token='736622043190296576-Ul3PpspS3IPw7rz8OfTJ7WX0XTAs15W'
access_token_secret='aPY7E2tNBCvQzKbePlbzkeOfujDhXOSVmapxUOy0BlUC0'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search(keyword,count=500)
data=pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['Tweets'])
print(data)
print(tweets[0].created_at)

df=pd.DataFrame(data=data)

df.to_csv("./file.csv", sep=',',index=False)
#df.to_csv("./file.csv")
