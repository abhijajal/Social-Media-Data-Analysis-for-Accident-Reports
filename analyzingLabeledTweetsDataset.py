i=1
file = open("labeledTweetDataset.txt",'r')
lines = file.readlines()
positiveExamples = 0
negativeExamples = 0
for eachLine in lines:
    if(eachLine.find("::::::1") >= 0):
        positiveExamples = positiveExamples + 1
    elif (eachLine.find("::::::0") >= 0):
        negativeExamples = negativeExamples + 1

    else:
        print(i)
    i = i + 1

print("Total Tweets: "+str(i-1))
print("No of Accidental tweets: "+str(positiveExamples))
print("No of Non-Accidental tweets: "+str(negativeExamples))
