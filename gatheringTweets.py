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
            if(status._json['lang']=='en'):
                if not status._json['retweeted'] and 'RT @' not in status._json['text']:
                    #Checking if the tweet is in english
                    print(len(status.text))
                    try:
                        print(status._json['extended_tweet']['full_text'])
                        file.write(status._json['extended_tweet']['full_text'].replace('\n',' ').strip()+"::::::\n")
                    except:
                        print(status.text)
                        file.write(status.text.replace('\n','\t').strip()+"::::::\n")

                    data.write(str(status._json) + "\n")



    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


data = open("data.json", "a+")
file = open("tweets.txt", "a+")

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
#keywords on which we will filter
sapi.filter(track=['accident','road','highway'])