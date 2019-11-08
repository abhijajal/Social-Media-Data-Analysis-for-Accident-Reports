dataSetFile = open("oldTweets.txt",'r')
lines = dataSetFile.readlines()
i=1
fileDivya = open("tweetDataset_Divya.txt",'w')
fileMatt = open("tweetDataset_Matt.txt",'w')
fileBanerjee = open("tweetDataset_Banerjee.txt",'w')
fileJacky = open("tweetDataset_Jacky.txt",'w')
fileJajal = open("tweetDataset_Jajal.txt",'w')
for eachLine in lines:
    if(i>0 and i<=1000):
        fileJajal.write(eachLine)
    elif(i>1000 and i<=2000):
        fileMatt.write(eachLine)
    elif (i > 2000 and i <= 3000):
        fileBanerjee.write(eachLine)
    elif (i > 3000 and i <= 4000):
        fileJacky.write(eachLine)
    elif (i > 4000):
        fileDivya.write(eachLine)
    i=i+1
