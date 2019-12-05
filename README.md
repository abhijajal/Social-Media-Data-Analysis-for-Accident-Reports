# Social-Media-Data-Analysis-for-Accident-Reports
This project collects social media data (from Twitter) and analyzes it to retrieve any roadside traffic accident related information (like the location of incident, severity, type of injuries, etc) in realtime. Python, Spark, Apache Kafka.

Please do add your API keys in apiKeys.py

## For Collecting Tweets
It will create a append only tweets.txt which will store the tweets.

You can run it by:
python gatheringTweets.py

## For Training the Model (Offline)

Run "trainModels.py" to train the Models offline for the data stored in finalDataSet.txt
After running this, two folders would be created for storing models.

## For Streaming 

Open the terminal and run zookeeper, Kafka Server and create a topic named "twitter"
Run "twitter_producer_location.py"
Run "twitter_producer_keyword.py"
Run "twitter_consumer.py"

## Visualization

Visualize the Data is Kibana at indexes twitternb and twitterlr

### Code for Running Kafka: 
Starting the zookeeper:
bin/zookeeper-server-start.sh config/zookeeper.properties

Starting the Kafka Server:
bin/kafka-server-start.sh config/server.properties

Creating a topic:
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic twitter

List all the topics:
bin/kafka-topics.sh --list --zookeeper localhost:2181

Running Producer:
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic twitter

Running Consumer:
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic twitter --from-beginning
