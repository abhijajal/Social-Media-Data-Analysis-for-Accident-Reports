import tweepy
import sys
import apiKeys

consumer_key=apiKeys.consumer_key
consumer_secret=apiKeys.consumer_secret
access_key=apiKeys.access_key
access_secret=apiKeys.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
            file.write(str(status)+"\n")
            print (status.text)


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


file = open("tweets.txt", "a+")
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=[-96.987075,32.625289,-96.562834,33.015838])