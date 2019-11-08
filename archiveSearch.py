import tweepy
# assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)
API_KEY = "uC0dz7UjkBeMJyPyEbbd5YHfA"
API_SECRET = "O90J8FxJibOoqzmXpQhGCZpMKNE3AwnRqONKYuRFHV8Mwpp1oK"
ACCESS_TOKEN_SECRET = "vFq7CoVYUObcVPZYA4auM5L4jxNYfpRLmfaNnpVauWK9u"
ACCESS_TOKEN = "805996119759192064-qxjj4Y1hzDt73xe10KMkqrJgijn3aSt"
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
data = open("archiveData.json", "a+")

query = 'accident OR interstate OR turnpike OR tollway'
file = open("oldTweets.txt",'a+')
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
        #print(new_tweets)
        for status in new_tweets:
            if (status._json['lang'] == 'en'):
                data.write(str(status._json) + "\n")
                if not status._json['retweeted'] and 'RT @' not in status._json['full_text']:
                    # Checking if the tweet is in english
                    data.write(str(status._json)+"\n")
                    try:
                        print(status._json['full_text'])
                        file.write(status._json['full_text'].replace('\n', ' ').strip() + "::::::\n")
                    except:
                        print(status.text)
                        file.write(status.text.replace('\n', ' ').strip() + "::::::\n")

        print(len(new_tweets))
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        print(e)
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break