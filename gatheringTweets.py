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
                        print(status._json['extended_tweet']['full_text'])
                        file.write(status._json['extended_tweet']['full_text'].replace('\n',' ').strip()+"::::::\n")
                    except:
                        print(status.text)
                        file.write(status.text.replace('\n',' ').strip()+"::::::\n")
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
sapi.filter(track=['accident','interstate','turnpike','tollway','sam rayburn','i-5','i-8','i-10','i-15','i-20','i-22','i-25','i-26','i-29','i-30','i-35','i-39','i-40','i-44','i-45','i-49','i-55','i-57','i-59','i-64','i-65','i-69','i-70','i-71','i-74','i-75','i-76','i-77','i-79','i-80','i-81','i-84','i-85','i-87','i-90','i-91','i-94','i-95','i-105','i-205','i-305','i-405','i-505','i-605','i-705','i-805','i-110','i-210','i-310','i-410','i-510','i-610','i-710','i-910','i-115','i-215','i-315','i-515','i-220','i-520','i-820','i-225','i-430','i-530','i-630','i-35e','i-35w','i-135','i-235','i-335','i-435','i-535','i-635','i-140','i-240','i-440','i-540','i-840','i-345','i-155','i-255','i-355','i-165','i-265','i-465','i-565','i-865','i-170','i-270','i-370','i-470','i-670','i-175','i-275','i-375','i-475','i-575','i-675','i-180','i-280','i-380','i-480','i-580','i-680','i-780','i-880','i-980','i-185','i-285','i-385','i-485','i-585','i-785','i-985','i-190','i-290','i-390','i-490','i-590','i-690','i-790','i-890','i-990','i-195','i-295','i-395','i-495','i-595','i-695','i-795','i-895'])