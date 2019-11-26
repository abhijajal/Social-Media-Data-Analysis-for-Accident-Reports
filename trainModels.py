from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from nltk.corpus import stopwords
from pyspark.ml.feature import RegexTokenizer, StopWordsRemover, CountVectorizer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.feature import HashingTF, IDF
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.classification import RandomForestClassifier
from pyspark.mllib.evaluation import MulticlassMetrics
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
sc =SparkContext()
sqlContext = SQLContext(sc)

sc.setLogLevel("WARN")


def lemma(x):
    print(x)
    lemmatizer = WordNetLemmatizer()
    print(lemmatizer.lemmatize(x))
    return lemmatizer.lemmatize(x)


def MF_map(line):
    data = [float(int(line[len(line)-1:])),line[:len(line)-7]]
    return data

def myprint(record):
    print(record)
    print('\n\n\n')

#Opening the file which cotains the data.
data = sc.textFile('finalDataset.txt')
#Splitting the class Labels and headline+Body
records = data.map(MF_map)

#Converting it into DataFrame
df = records.toDF()
#Regular expression tokenizer
df = df.withColumnRenamed("_1","label")
regexTokenizer = RegexTokenizer(inputCol="_2", outputCol="words", pattern="\\W")
#StopWords Removal
add_stopwords = stopwords.words('english')
stopwordsRemover = StopWordsRemover(inputCol="words", outputCol="filtered").setStopWords(add_stopwords)
hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=10000)
#IF-IDF
tfIdf = IDF(inputCol="rawFeatures", outputCol="features", minDocFreq=5) #minDocFreq: remove sparse terms

#For Logistic Regression
lr = LogisticRegression(maxIter=50, regParam=0.3, elasticNetParam=0)
pipeline1 = Pipeline(stages=[regexTokenizer, stopwordsRemover, hashingTF, tfIdf,lr])
(trainingData, testData) = df.randomSplit([0.6, 0.4], seed = 100)
pipelineFit1 = pipeline1.fit(trainingData)
predictions1 = pipelineFit1.transform(testData)
evaluator1 = MulticlassClassificationEvaluator()
accuracy1 = evaluator1.evaluate(predictions1, {evaluator1.metricName: "accuracy"})
predictions1.show(20)
path1="APJ180001_lr.model"
pipelineFit1.write().overwrite().save(path1)
print("Logistic Regression:",accuracy1)
predictionAndLabels = predictions1.select("prediction", "label").rdd.map(lambda r : (r[0], r[1]))
metrics1 = MulticlassMetrics(predictionAndLabels)

#Overall statistics
precision1 = metrics1.precision()
recall1 = metrics1.recall()
f1Score1 = metrics1.fMeasure()

print("Summary Stats")
print("Precision = %s" % precision1)
print("Recall = %s" % recall1)
print("F1 Score = %s" % f1Score1)

#Naive Bayesian
nb = NaiveBayes(smoothing=1)
pipeline2 = Pipeline(stages=[regexTokenizer, stopwordsRemover, hashingTF, tfIdf,nb])
pipelineFit2 = pipeline2.fit(trainingData)
predictions2 = pipelineFit2.transform(testData)
evaluator2 = MulticlassClassificationEvaluator()
accuracy2 = evaluator2.evaluate(predictions2, {evaluator2.metricName: "accuracy"})
predictions2.show(20)
path2="APJ180001_nb.model"
pipelineFit2.write().overwrite().save(path2)
print("Naive Bayes:",accuracy2)

predictionAndLabels2 = predictions2.select("prediction", "label").rdd.map(lambda r : (r[0], r[1]))
# Instantiate metrics object
metrics2 = MulticlassMetrics(predictionAndLabels2)

# Overall statistics
precision2 = metrics2.precision()
recall2 = metrics2.recall()
f1Score2 = metrics2.fMeasure()

print("Summary Stats")
print("Precision = %s" % precision2)
print("Recall = %s" % recall2)
print("F1 Score = %s" % f1Score2)
