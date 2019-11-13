i=1
file = open("tweetDataset_Matt.txt",'r')
lines = file.readlines()
for eachLine in lines:
    if(eachLine.find("::::::1") >= 0 or eachLine.find("::::::0") >= 0):
        pass
    else:
        print(i)
    i = i + 1
print(i)