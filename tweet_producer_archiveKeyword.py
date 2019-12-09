# -*- coding: utf-8 -*-

from kafka import KafkaProducer
from time import sleep
import json, sys
import requests
import time
import tweepy
import sys
import apiKeys

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

if __name__== "__main__":
    
    if len(sys.argv) != 1:
        print ('Number of arguments is not correct')
        exit()

    consumer_key = apiKeys.consumer_key
    consumer_secret = apiKeys.consumer_secret
    access_key = apiKeys.access_key
    access_secret = apiKeys.access_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)
    data = open("archiveData.json", "a+")

    query = 'accident'
    max_tweets = 10000
    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, tweet_mode='extended', count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            for status in new_tweets:
                sentence=""
                #print(status)
                if (status._json['lang'] == 'en'):
                    #data.write(str(status._json) + "\n")
                    if not status._json['retweeted'] and 'RT @' not in status._json['full_text']:
                        # Checking if the tweet is in english
                        #data.write(str(status._json) + "\n")
                        try:
           #                 print(status._json['full_text'])
                            sentence=status._json['full_text'].replace('\n', ' ').strip() + "::::::"+status._json['created_at']
                        except:
            #                print(status.text)
                            sentence=status.text.replace('\n', ' ').strip() + "::::::"+status._json['created_at']

                    print(sentence)
                    if(len(sentence.strip())>0):
                        prod = connect_kafka_producer();
                        publish_message(prod, 'twitter', sentence)
                        if prod is not None:
                            prod.close()
                        sleep(5)
            print(len(new_tweets))
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print(e)
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            break