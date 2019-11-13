dataSetFile = open("labeledTweetDataset.txt",'w+')
lines = dataSetFile.readlines()
i=1
fileDivya = open("tweetDataset_Divya.txt",'r')
fileMatt = open("tweetDataset_Matt.txt",'r')
fileBanerjee = open("tweetDataset_Banerjee.txt",'r')
fileJacky = open("tweetDataset_Jacky.txt",'r')
fileJajal = open("tweetDataset_Jajal.txt",'r')
lines = fileJajal.readlines()
for eachLine in lines:
    dataSetFile.write(eachLine)

lines = fileMatt.readlines()
for eachLine in lines:
    dataSetFile.write(eachLine)

lines = fileBanerjee.readlines()
for eachLine in lines:
    dataSetFile.write(eachLine)

lines = fileJacky.readlines()
for eachLine in lines:
    dataSetFile.write(eachLine)

lines = fileDivya.readlines()
for eachLine in lines:
    dataSetFile.write(eachLine)
