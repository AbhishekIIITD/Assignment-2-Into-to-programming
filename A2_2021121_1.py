from random import choice
def wordscount(listofwords):
    dic=dict()
    for i in range(0,len(listofwords)):
        for j in range(0,len(listofwords[i])):
            if listofwords[i][j] not in dic:
                dic[listofwords[i][j]]=1
            else:
                dic[listofwords[i][j]]+=1
    return dic
            
def replacefromfile(y,file_name):
    with open(file_name,"w") as f:
        f.write(y)
        print("Successfully changed")


def countword(list_of_words,x):
    count=0
    for i in list_of_words:
        if i==x:
            count+=1
    return count

print("Enter your choice : \n1. Display Specific word count : \n2. Display all unique words : \n3. Display all word count : \n4. Replace word \n5. Quit")
choice=int(input())

with open("question1_input.txt","r") as f:
    data=f.readlines()
    if choice==1:
        count=0
        x=input("Enter the word : ")
        for i in data:
            listx=i.split()
            counti=countword(listx,x)
            count=count+counti
        print(count)
    elif choice==2:
        for i in range(0,len(data)):
            data[i]=data[i].split()
        words=wordscount(data)
        for i in words.keys():
            if(words[i]==1):
                print(i,end=" ; ")
    elif choice==3:
        for i in range(0,len(data)):
            data[i]=data[i].split()
        words=wordscount(data)
        for i in words.keys():
            print(i," : ",words[i])
    elif choice==4:
        rword=input("Enter the word to be replaced : ")
        lword=input("Enter the word with which you want it to be replaced : ")
        for i in range(0,len(data)):
            data[i]=data[i].split()
        for i in range(0,len(data)):
            for j in range(0,len(data[i])):
                if data[i][j]==rword:
                    data[i][j]=lword
        for i in range(0,len(data)):
            data[i]=" ".join(data[i])
        y=" ".join(data)
        replacefromfile(y,"A1_2021121_1.txt")






        
        


