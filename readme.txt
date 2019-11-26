Steps for runnning this Project:

1. Run "trainModels.py" to train the Models offline for the data stored in finalDataSet.txt.
2. After running this, two folders would be created for storing models.
3. Then open the terminal and run zookeeper, Kafka Server and create a topic named "twitter"
4. Run "twitter_producer.py" 
5. Run "twitter_consumer.py" 
6. Visualize the Data is Kibana at indexes twitternb and twitterlr

Code for Running Kafka: 
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

