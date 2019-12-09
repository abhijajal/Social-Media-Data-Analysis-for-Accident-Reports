import nltk
import spacy
from nltk.stem import WordNetLemmatizer
from spacy.matcher import Matcher
from nltk.tag import StanfordNERTagger
import pandas as pd
from subprocess import call
import severity_classifier
import re
processedTweets=[]
from elasticsearch import Elasticsearch
es=Elasticsearch([{'host':'localhost','port':9200}])
indexName2="taccidental"
typeName2="accidental"

pd.set_option('display.max_colwidth', 200)



def penn_to_wn(tag):
  """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
  if tag.startswith('N'):
    return 'n'

  if tag.startswith('V'):
    return 'v'

  if tag.startswith('J'):
    return 'a'

  if tag.startswith('R'):
    return 'r'

  return None


def isAlredyPresent(sentence):
  if(len(processedTweets)==0):
    return False
  else:
    try:
      if(processedTweets.index(sentence)>=0):
        return True
      else:
        return False
    except:
      return False


def task2(sentence,timestamp):
  # loading spacy model
  nlp = spacy.load("en_core_web_sm")
  import en_core_web_sm
  nlp = en_core_web_sm.load()

  print(sentence)
  if (isAlredyPresent(sentence) == False):
    processedTweets.append(sentence)
    call(["aplay", "Air.wav"])
    doc = nlp(sentence)
 #   print(sutime.SUTime(sentence))
    #  print([(X.text, X.label_) for X in doc.ents])

    # Tokenization
    tokens = []
    tokens = nltk.word_tokenize(sentence);
    #print("Tokens: ", tokens)
    #  tweetFile = open("stanford-ner-2018-10-16/tweet.txt", 'w')

    nlp = spacy.load("en_core_web_sm")
    # Matcher class object
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", None, [{'POS': 'PROPN'}, {'LOWER': {'IN': ['ave', 'avenue', 'st', 'street',
                                                                       'rd', 'road', 'dr', 'drive', 'pkwy', 'parkway',
                                                                       'bend', 'bnd', 'boulevard', 'blvd', 'court',
                                                                       'ct',
                                                                       'expressway', 'expy', 'freeway', 'fwy',
                                                                       'highway', 'hwy', 'junction', 'jct', 'lane',
                                                                       'ln', 'loop', 'motorway', 'mtwy',
                                                                       'parkway', 'pkwy', 'point', 'pt', 'ramp',
                                                                       'turnpike', 'tpke', 'tunnel', 'tunl',
                                                                       'underpass']}}])

    matches = matcher(doc)
    span = ""
    for match_id, start, end in matches:
        span = doc[start:end]
    # print(span)

    st = StanfordNERTagger('stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
                           "stanford-ner-2018-10-16/stanford-ner.jar", encoding='utf-8')
    classifiedText = st.tag(tokens)
    location = ""
    #print(classifiedText)
    i = 0
    locationMatches = []
    for eachOut in classifiedText:
        if "LOCATION" in eachOut[1]:
            locationMatches.append(eachOut[0])
    # print(locationMatches)
    span = str(span)
    #print(span)
    # Lemmatization without POS tags
    lems = []
    lemmatizer = WordNetLemmatizer()
    pos_sen = nltk.pos_tag(tokens);
    #print("\n POS Tags: \n", pos_sen);

    pos_wn = [(s[0], penn_to_wn(s[1])) for s in pos_sen]
    # print("\n POS Tags for wordnet: \n", pos_wn)

    lems_pos = []
    for w in pos_wn:
        if (w[1]):
            lems_pos.append(lemmatizer.lemmatize(w[0], pos=w[1]))
        else:
            lems_pos.append(lemmatizer.lemmatize(w[0]))
    # print("\n Lemmatization by taking into account the pos tags: \n")
    # print(lems_pos)

    if("on" in tokens):
        try:
            x = tokens.index("on")
            x+=1
            while pos_sen[x][1]=="NNP":
                if pos_sen[x][0] not in locationMatches:
                    locationMatches.append(pos_sen[x][0])
                x+=1
            if(pos_sen[x][1]=="CD" and pos_sen[x+1][1]=="NNP" and pos_sen[x+1][0]!="AM" and pos_sen[x+1][0]!="am" and pos_sen[x+1][0]!="pm" and pos_sen[x+1][0]!="PM" ):
                if pos_sen[x][0] not in locationMatches:
                    locationMatches.append(pos_sen[x][0])

                if pos_sen[x+1][0] not in locationMatches:
                    locationMatches.append(pos_sen[x+1][0])

                x+=1
                x+=1
                while pos_sen[x][1] == "NNP":
                    if pos_sen[x][0] not in locationMatches:
                        locationMatches.append(pos_sen[x][0])
                    x += 1



        except:
            pass

    if ("at" in tokens):
        try:
            x = tokens.index("at")
            x += 1
            while pos_sen[x][1] == "NNP":
                if pos_sen[x][0] not in locationMatches:
                    locationMatches.append(pos_sen[x][0])
                x+=1
            if (pos_sen[x][1] == "CD" and pos_sen[x + 1][1] == "NNP" and pos_sen[x+1][0]!="AM" and pos_sen[x+1][0]!="am" and pos_sen[x+1][0]!="pm" and pos_sen[x+1][0]!="PM" ):
                if pos_sen[x][0] not in locationMatches:
                    locationMatches.append(pos_sen[x][0])

                if pos_sen[x + 1][0] not in locationMatches:
                    locationMatches.append(pos_sen[x + 1][0])

                x += 1
                x += 1
                while pos_sen[x][1] == "NNP":
                    if pos_sen[x][0] not in locationMatches:
                        locationMatches.append(pos_sen[x][0])
                    x += 1

        except:

            pass

    if ("AT" in tokens):
        try:
            x = tokens.index("AT")
            x += 1
            while pos_sen[x][1] == "NNP":
                if pos_sen[x][0] not in locationMatches:
                    locationMatches.append(pos_sen[x][0])
                x+=1
            if (pos_sen[x][1] == "CD" and pos_sen[x + 1][1] == "NNP" and pos_sen[x+1][0]!="AM" and pos_sen[x+1][0]!="am" and pos_sen[x+1][0]!="pm" and pos_sen[x+1][0]!="PM" ):
                if pos_sen[x][0] not in locationMatches:
                    locationMatches.append(pos_sen[x][0])

                if pos_sen[x + 1][0] not in locationMatches:
                    locationMatches.append(pos_sen[x + 1][0])

                x += 1
                x += 1
                while pos_sen[x][1] == "NNP":
                    if pos_sen[x][0] not in locationMatches:
                        locationMatches.append(pos_sen[x][0])
                    x += 1

        except:
            pass
    #print(locationMatches)
    removal=[]
    if (len(locationMatches) > 0 and len(span) > 0):
        for eachMatch in locationMatches:
            #print(len(locationMatches))
            try:
                #print(span.find(eachMatch))
                if span.find(eachMatch) != -1:
                    removal.append(eachMatch)
            except:
                print("Exception Distinct")

        for removeItem in removal:
            locationMatches.remove(removeItem)

    location= (span + " " + " ".join(locationMatches)).strip()


    #Extracting Time using Regular Expression:
    re6 = r"(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]:[0-5][0-9])([\s]*[AaPp][Mm])"
    re2 = r"(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]:[0-5][0-9])"
    re3 = r"24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]([\s]*[AaPp][Mm])"
    re4 = r"24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]"
    re5 = r"([0-9][0-9]?:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])([\s]*[AaPp]*[Mm]*)"
    re1 = r"([0-9][0-9]*:[0-5][0-9]:[0-5][0-9])([\s]*[AaPp]*[Mm]*)"
    re7 = r"([0-9][0-9]*:[0-5][0-9])"

    try:
        time=(re.compile("(%s|%s|%s|%s|%s|%s|%s)" % (re1, re2, re3, re4, re5, re6, re7)).findall(sentence))[0][0]
        time=str(time)
        if(len(time.strip())>0):
            print("Time: "+str(time))
            timestamp=time
    except BaseException as e:
        print("Time : "+timestamp)


    severity= severity_classifier.severity_finder(sentence)
    severityStr=""
    for eachKeyword in severity:
        severityStr+=str(eachKeyword)+" "
    print("Severity: "+severityStr)

    if (len(location) > 0):
        print("Location: " + location)
        e2 = {"predictedClassLabel": "Accidental", "tweet": sentence, "timestamp": timestamp, "location":location,"severity":severityStr}
    else:
        e2 = {"predictedClassLabel": "Accidental", "tweet": sentence, "timestamp": timestamp,"severity":severityStr}
    res2 = es.index(index=indexName2, doc_type=typeName2, body=e2)


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# newPositiveDataSetFile = open("positiveDataset.txt", 'r+')
#
# lines = newPositiveDataSetFile.readlines()
# for eachLine in lines:
#      task2(eachLine,"timestamp")
task2("IH-610 NORTH LOOP Westbound At IH-45 NORTH - Accident - Status: Verified at 4:20 PM - Lanes Affected: 2 Mainlane(s)","s")