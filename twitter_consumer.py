from kafka import KafkaConsumer
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import HashingTF, IDF
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.feature import RegexTokenizer, StopWordsRemover, CountVectorizer
from pyspark.ml import PipelineModel
from pyspark.ml.feature import Tokenizer, RegexTokenizer
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
from pyspark.sql import Row
from subprocess import call
import time
import requests
import subprocess
from pyspark.mllib.evaluation import MulticlassMetrics
from elasticsearch import Elasticsearch
es=Elasticsearch([{'host':'localhost','port':9200}])
indexName="twitternb"
indexName2="twitterlr"
typeName1="NaiveB"
typeName2="logisticR"
# import pyspark.sql.Row
# import pyspark.implicits._
sc =SparkContext()
sqlContext = SQLContext(sc)
consumer = KafkaConsumer('twitter',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
nbModel = PipelineModel.load("APJ180001_nb.model")
lrModel = PipelineModel.load("APJ180001_lr.model")

evaluator = MulticlassClassificationEvaluator()
count=0;
sum=0;
avg=0;
sum2=0
count2=0
labels={}
index = 0

accidentalTweetsNB = open("accidentalTweetsNB.txt", 'a+')
accidentalTweetsLR = open("accidentalTweetsLR.txt", 'a+')

for message in consumer:
    consumer.commit() 
    message=message.value.decode('utf-8')
    print(message)
    messages= message.split("::::::")
    timestamp=messages[1]
    text=messages[0]
    message=sc.parallelize([(timestamp, text)])
    records = message.map(lambda row: Row(timeStamp=row[0],_2=row[1]))
    df=sqlContext.createDataFrame(records)

    # For Naive Baiysian
    predictions = nbModel.transform(df)
    predictions.show()
    asrr = predictions.select("prediction").take(1)
    strAsrr=str(asrr[0])[15:]
    x= strAsrr.find(')')
    predictedClass=int(float(strAsrr[:x]))
    if(predictedClass==1):
        predictedCategory="Accidental"
   #     call(["aplay", "Air.wav"])
        accidentalTweetsNB.write(text+"::::::"+timestamp+"\n")
    elif(predictedClass==0):
        predictedCategory="Non-Accidental"
    e1 = {"predictedClassLabel": predictedCategory, "tweet":text, "timestamp":timestamp}
    res = es.index(index=indexName, doc_type=typeName1, body=e1)


    # For Logistic Regression
    predictions2 = lrModel.transform(df)
    predictions2.show()
    asrr2 = predictions2.select("prediction").take(1)
    strAsrr2 = str(asrr2[0])[15:]
    x2 = strAsrr2.find(')')
    predictedClass2 = int(float(strAsrr2[:x2]))
    if (predictedClass2 == 1):
        predictedCategory2 = "Accidental"
        call(["aplay", "Air.wav"])
        accidentalTweetsLR.write(text+"::::::"+timestamp+"\n")

    elif (predictedClass2 == 0):
        predictedCategory2 = "Non-Accidental"
    e2 = {"predictedClassLabel": predictedCategory2, "tweet":text, "timestamp":timestamp}
    res2 = es.index(index=indexName2, doc_type=typeName2, body=e2)
