Steps for runnning HW3:

1. Run "trainModels.py" to train the Models offline for the data stored in dataSet.txt.
2. After running this, two folders would be created for storing models named "" and ""
3. Then open the terminal and run zookeeper, Kafka Server and create a topic named "gaurdian2"
4. Run "stream_producer.py" with following parameters : API_KEY 2019-09-02 2019-11-01
5. Run "stream_consumer.py" 
6. Visualize the Data is Kibana at indexes bigdatahwnb and bigdatahwlr

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

dataSet.txt cotains the data collected from Gaurdian API, it cotains 5184 news articles.

By: APJ180001