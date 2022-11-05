def getReverse(n):
    res=""
    n=str(n)
    l=len(n)-1
    while(l>=0):
        res=res+n[l]
        l-=1
    res=int(res)
    return res

def testing(N):
    for i in range(N):
        with open(f"input{i+1}.txt","r") as inputs:
            data=int(inputs.read())
            test=getReverse(data)
            with open(f"output{i+1}.txt","r") as output:
                outres=int(output.read())
                if(test!=outres):
                    return "Failed"
    return "SUCCESS"                    

print(testing(5))

