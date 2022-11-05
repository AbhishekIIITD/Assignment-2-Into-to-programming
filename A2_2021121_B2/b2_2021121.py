p,q=map(int,input().split())
m,n=map(int,input().split())
flag=0
dojarep=0
djrep=0
skyscrapers=[]
nexttall=0
occupied=0
for i in range(m):
    temp=input()
    skyscrapers.append(temp)
while(occupied<n):
    build=0
    for i in range(0,m):
        for j in range(0,n):
            flag1=0
            if(skyscrapers[i][j]=="1"):
                nexttall=i
                build=j
                flag1=1
                break
        if(flag1):
            break
        
    print(nexttall,build)
    if(flag==0):
        dojarep+=p*(m-nexttall)
        for i in range(nexttall,m):
            data=skyscrapers[i]
            data=data[0:build]+"D"+data[build+1:]
            skyscrapers[i]=data
        flag=1

            
    elif(flag==1):
        djrep+=q*(m-nexttall)
        for i in range(nexttall,m):
            data=skyscrapers[i]
            data=data[0:build]+"S"+data[build+1:]
            skyscrapers[i]=data
        flag=0
    p+=1
    q+=1
    occupied+=1

print("Reputation of doja is :",dojarep)
print("Reputtion of dj snake is :",djrep)

for i in range(0,m):
    print(skyscrapers[i])
    

    
    




    



