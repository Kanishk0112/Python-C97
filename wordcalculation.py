info=input("Enter Your Introduction")
charactercount=0
wordcount=1
for i in info:
    charactercount=charactercount+1
    if(i==" "):
        wordcount=wordcount+1
print("number of words in a string")
print(wordcount)
print("number of characters in a string")
print(charactercount)