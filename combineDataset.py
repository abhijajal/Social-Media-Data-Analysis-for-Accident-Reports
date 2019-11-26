newDataSetFile = open("finalDataset.txt", 'w+')
i=1
fileOurLabelledTweets = open("labeledTweetDataset.txt",'r')
fileBoston = open("Boston4C.csv",'r')
fileChicago = open("Chicago4C.csv",'r')
fileMemphis = open("Memphis4C.csv",'r')
fileNYC = open("NYC4C.csv",'r')
fileSanF = open("SanFrancisco4Classes.csv",'r')
fileSeattle = open("Seattle4Classes.csv",'r')


lines = fileOurLabelledTweets.readlines()
for eachLine in lines:
    newDataSetFile.write(eachLine)
    i=i+1
print(i)

lines = fileBoston.readlines()
for eachLine in lines:
    fields=eachLine.split(';');
    if(len(fields)== 3):
        tweet= fields[1]+"::::::"
        fields[2]= fields[2].strip('\n')
        if(fields[2]=="fire" or fields[2]=="shooting" or fields[2]=="NO" or fields[2]=="fire\n" or fields[2]=="shooting\n" or fields[2]=="NO\n"):
            tweet+="0\n"
        elif(fields[2] == "crash" or fields[2] == "crash\n"):
            tweet+="1\n"
        else:
            print("error")
            print(fields[2]+"XX")
        newDataSetFile.write(tweet)
        i=i+1
print(i)

lines = fileChicago.readlines()
for eachLine in lines:
    fields=eachLine.split(';');
    if(len(fields)== 3):
        tweet = fields[1] + "::::::"
        fields[2] = fields[2].strip('\n')
        if (fields[2]=="fire" or fields[2]=="shooting" or fields[2]=="NO" or fields[2]=="fire\n" or fields[2]=="shooting\n" or fields[2]=="NO\n"):
            tweet += "0\n"
        elif (fields[2] == "crash" or fields[2] == "crash\n"):
            tweet += "1\n"
        else:
            print("error")
            print(fields[2]+"XX")
        newDataSetFile.write(tweet)
        i=i+1
print(i)

lines = fileMemphis.readlines()
for eachLine in lines:
    fields=eachLine.split(';');
    if(len(fields)== 3):
        tweet = fields[1] + "::::::"
        fields[2] = fields[2].strip('\n')
        if (fields[2]=="fire" or fields[2]=="shooting" or fields[2]=="NO" or fields[2]=="fire\n" or fields[2]=="shooting\n" or fields[2]=="NO\n"):
            tweet += "0\n"
        elif (fields[2] == "crash" or fields[2] == "crash\n"):
            tweet += "1\n"
        else:
            print("error")
            print(fields[2]+"XX")
        newDataSetFile.write(tweet)

        i=i+1
print(i)

lines = fileNYC.readlines()
for eachLine in lines:
    fields=eachLine.split(';');

    if(len(fields)== 3):
        tweet = fields[1] + "::::::"
        fields[2] = fields[2].strip('\n')
        if (fields[2]=="fire" or fields[2]=="shooting" or fields[2]=="NO" or fields[2]=="fire\n" or fields[2]=="shooting\n" or fields[2]=="NO\n"):
            tweet += "0\n"
        elif (fields[2] == "crash" or fields[2] == "crash\n"):
            tweet += "1\n"
        else:
            print("error")
            print(fields[2]+"XX")
        newDataSetFile.write(tweet)

        i=i+1
print(i)

lines = fileSanF.readlines()
for eachLine in lines:
    fields=eachLine.split(';');
    if(len(fields)== 3):
        tweet = fields[1] + "::::::"
        if (fields[2]=="fire" or fields[2]=="shooting" or fields[2]=="NO" or fields[2]=="fire\n" or fields[2]=="shooting\n" or fields[2]=="NO\n"):
            tweet += "0\n"
        elif (fields[2] == "crash" or fields[2] == "crash\n"):
            tweet += "1\n"
        else:
            print("error")
            print(fields[2]+"XX")
        newDataSetFile.write(tweet)

        i=i+1
print(i)

lines = fileSeattle.readlines()
for eachLine in lines:
    fields=eachLine.split(';');
    if(len(fields)== 3):
        tweet = fields[1] + "::::::"
        fields[2] = fields[2].strip('\n')
        if (fields[2]=="fire" or fields[2]=="shooting" or fields[2]=="NO" or fields[2]=="fire\n" or fields[2]=="shooting\n" or fields[2]=="NO\n"):
            tweet += "0\n"

        elif (fields[2] == "crash" or fields[2] == "crash\n"):
            tweet += "1\n"

        else:
            print("error")
            print(fields[2]+"XX")
        newDataSetFile.write(tweet)


        i=i+1
print(i)

