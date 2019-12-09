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
import big_data

from elasticsearch import Elasticsearch
es=Elasticsearch([{'host':'localhost','port':9200}])
indexName1="tnonaccidental"
indexName2="taccidental"
typeName1="nonAccidental"
typeName2="accidental"
# import pyspark.sql.Row
# import pyspark.implicits._
sc =SparkContext()
sqlContext = SQLContext(sc)
consumer = KafkaConsumer('twitter',
                         group_id='twitter',
                         bootstrap_servers=['localhost:9092'],max_poll_records=10)
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
    message = message.value.decode('utf-8')

    if(len(message.strip())>0):
        #print(message)
        messages= message.split("::::::")
        timestamp=messages[1]
        text=messages[0]
        message=sc.parallelize([(timestamp, text)])
        records = message.map(lambda row: Row(timeStamp=row[0],_2=row[1]))
        df=sqlContext.createDataFrame(records)

        # For Logistic Regression
        predictions2 = lrModel.transform(df)
        #predictions2.show()
        asrr2 = predictions2.select("prediction").take(1)
        strAsrr2 = str(asrr2[0])[15:]
        x2 = strAsrr2.find(')')
        predictedClass2 = int(float(strAsrr2[:x2]))
        if (predictedClass2 == 1):
            predictedCategory2 = "Accidental"
            accidentalTweetsLR.write(text+"::::::"+timestamp+"\n")
            big_data.task2(text,timestamp)

        elif (predictedClass2 == 0):
            predictedCategory2 = "Non-Accidental"
            e2 = {"predictedClassLabel": predictedCategory2, "tweet":text, "timestamp":timestamp}
            res2 = es.index(index=indexName1, doc_type=typeName1, body=e2)
