
finaldata=[]

with open("Admin/RegisteredStudents.txt","r") as rs:
    with open("Admin/AnswerKey.txt","r") as answers:
        answerkey=answers.readlines()
        ans=dict()
        for i in range(0,len(answerkey)):
            answerkey[i]=answerkey[i].split()
        for i in range(0,len(answerkey)):
            ans[answerkey[i][0]]=answerkey[i][1]



        data =rs.readlines()
        for i in data:
            x=i.split()
            name=x[0]
            rollno=x[1]
            with open("Student/"+name+"_"+rollno+".txt","r") as sd:
                studentres=sd.readlines()
                marks=0
                for i in range(0,len(answerkey)):
                    choosen=studentres[i].split()
                    if(choosen[1]==ans[choosen[0]]):
                        marks+=4
                    elif(choosen[1]!=ans[choosen[0]] and choosen[1]!="-"):
                        marks-=1
                    else:
                        marks+=0
                marksofstud=[name,rollno,str(marks)]
                finaldata.append(marksofstud)
for i in range(0,len(finaldata)):
    finaldata[i]=" ".join(finaldata[i])
finaldata="\n".join(finaldata)
with open("finalreport.txt","w") as f:
    f.write(finaldata)

