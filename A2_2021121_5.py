notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]


def noteCreate():

    with open("scalemajor.txt","w") as major:
        data=[]
        for i in range(0,len(notes)):
            key=[]
            j=i
            steps=0
            while(steps<=7):
                if(j>=len(notes)):
                    j=j%len(notes)
                
                key.append(notes[j])
                if(key[-1]==key[0] and len(key)>1):
                    key[-1]+="'"
                
                if(steps==2 or steps==6):
                    j=j+1
                else:
                    j+=2
                steps+=1
            key=" ".join(key)
            data.append(key)
        data="\n".join(data)
        major.write(data)
    with open("scaleminor.txt","w") as minor:
        data=[]
        for i in range(0,len(notes)):
            key=[]
            j=i
            steps=0
            while(steps<=7):
                if(j>=len(notes)):
                    j=j%len(notes)
                key.append(notes[j])
                if(key[-1]==key[0] and len(key)>1):
                    key[-1]+="'"
                
                if(steps==1 or steps==4):
                    j=j+1
                else:
                    j+=2
                steps+=1
            key=" ".join(key)
            data.append(key)
        data="\n".join(data)
        minor.write(data)
noteCreate()
def majorNotes(root):
    with open("scalemajor.txt","r") as major:
        data =major.readlines()
        for i in data:
            if i[0]==root:
                return i
        return "not found"
          
def minorNotes(root):
    with open("scaleminor.txt","r") as minor:
        data =minor.readlines()
        for i in data:
            if i[0]==root:
                return i
        return "not found"
          
root=input("Enter the root note : ")
scale=input("Enter the type of scale : ")
print(f"The {scale} scale in the key of C is : ",majorNotes(root) if scale=="major" else minorNotes(root))


            