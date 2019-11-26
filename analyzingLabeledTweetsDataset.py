i=1
file = open("finalDataset.txt",'r')
lines = file.readlines()
positiveExamples = 0
negativeExamples = 0
for eachLine in lines:
    label = eachLine[len(eachLine)-2:]
    if(label == "1\n"):
        positiveExamples = positiveExamples + 1
    elif (label == "0\n"):
        negativeExamples = negativeExamples + 1
    else:
        print(label)
        print(i)
    i = i + 1

print("Total Tweets: "+str(i-1))
print("No of Accidental tweets: "+str(positiveExamples))
print("No of Non-Accidental tweets: "+str(negativeExamples))
