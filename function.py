
f=open('text.txt')
fileLines=f.readlines()
for line in fileLines:
    print(line)
intro='my name is hriddhima , i am 15 years old.' 
words=intro.split("hriddhima")  
print(words)

def countWordsFromFile():
    fileName=input("enter the file name")
    noOfWords=0
    file=open(fileName,"r")
    for line in file:
        words=line.split()
        noOfWords= noOfWords+len(words)
    print("no. of words in the file are",noOfWords)
    

countWordsFromFile()

def greet(name):
    print('hello '+name+". How are you?")

greet("hriddhima")
