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
    count = 1
    def on_status(self, status):
            if(status._json['lang']=='en'):
                if not status._json['retweeted'] and 'RT @' not in status._json['text']:
                    #Checking if the tweet is in english
                    print(self.count)
                    try:
                        print(status._json['extended_tweet']['full_text']+"\n"+status._json['created_at'])
                        file.write(status._json['extended_tweet']['full_text'].replace('\n',' ').strip()+"::::::"+status._json['created_at']+"\n")
                    except:
                        print(status.text+"\n"+status._json['created_at'])
                        file.write(status.text.replace('\n',' ').strip()+"::::::"+status._json['created_at']+"\n")
                    self.count=self.count+1
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
sapi.filter(locations=[-96.987075,32.625289,-96.562834,33.015838])