newPositiveDataSetFile = open("positiveDataset.txt", 'w+')
i=1
finalLabelledTweets = open("finalDataset.txt", 'r')


lines = finalLabelledTweets.readlines()
for eachLine in lines:
    fields=eachLine.split('::::::');
    if(fields[1]=="1" or fields[1]=="1\n"):
        i = i + 1
        newPositiveDataSetFile.write(fields[0]+"\n")

print(i)

