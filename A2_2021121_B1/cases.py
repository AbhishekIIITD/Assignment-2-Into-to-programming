def getReverse(n):
    res=0
    while(n>0):
        res=res*10+n%10
        n=n//10


    
    return res


def generatedata(N):
    for i in range(N):
        x=int(input("please enter a num : "))
        with open("input"+str(i+1)+".txt","w") as inputs:
            inputs.write(str(x))

n=int(input("Enter the value of N : "))
generatedata(n)
for i in range(n):
    with open(f"input{str(i+1)}.txt","r") as inputs:
        data=int(inputs.read())
        with open(f"output{i+1}.txt","w") as output:
            res=getReverse(data)
            output.write(str(res))



        

