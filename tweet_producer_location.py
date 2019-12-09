# -*- coding: utf-8 -*-

from kafka import KafkaProducer
from time import sleep
import json, sys
import requests
import time
import tweepy
import sys
import apiKeys2

def publish_message(producer_instance, topic_name, value):
    try:
        key_bytes = bytes('foo', encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))

def connect_kafka_producer():
    _producer = None
    try:
        #_producer = KafkaProducer(value_serializer=lambda v:json.dumps(v).encode('utf-8'),bootstrap_servers=['localhost:9092'], api_version=(0, 10),linger_ms=10)
         _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10),linger_ms=10)
    
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

class CustomStreamListener(tweepy.StreamListener):
    count = 1
    def on_status(self, status):
            if(status._json['lang']=='en'):
                if not status._json['retweeted'] and 'RT @' not in status._json['text']:
                #Checking if the tweet is in english
                    print(self.count)
                    try:
                        tweet= status._json['extended_tweet']['full_text'].replace('\n',' ').strip()+"::::::"+status._json['created_at']
                    except:
                        tweet=status.text.replace('\n',' ').strip()+"::::::"+status._json['created_at']

                    prod = connect_kafka_producer();

                    print(json.dumps(tweet))
                    publish_message(prod, 'twitter', tweet)

                    if prod is not None:
                        prod.close()
                    self.count=self.count+1
                    file.write(tweet+"\n")
                    data.write(str(status._json) + "\n")
                    #sleep(20)


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream



if __name__== "__main__":
    
    if len(sys.argv) != 1:
        print ('Number of arguments is not correct')
        exit()

    consumer_key = apiKeys2.consumer_key
    consumer_secret = apiKeys2.consumer_secret
    access_key = apiKeys2.access_key
    access_secret = apiKeys2.access_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    data = open("data.json", "a+")
    file = open("tweets.txt", "a+")

    sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
    # keywords on which we will filter
    # Dallas:- 
    sapi.filter(locations=[-96.987075, 32.625289, -96.562834, 33.015838],is_async=True)
    # Texas:-
    #sapi.filter(locations=[-105.705273, 27.022092, -93.861037, 36.593243])

    # DFW:-
    #sapi.filter(locations=[-97.458277, 32.725528, -97.230735, 32.778289])
