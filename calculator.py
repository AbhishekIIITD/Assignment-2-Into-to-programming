class calculator:
    def __init__(self):
        self.calulator=True
    def add(self,l):
        res=0
        for i in range(0,len(l)):
            res+=l[i]
        return res
    def subtract(Self,l):
        res=l[0]
        res=float(res)
        for i in range(1,len(l)):
            res=res-l[i]
        return res
    def multiply(self,l):
        res=1
        for i in range(0,len(l)):
            res=res*l[i]
        return res
    def divide(self,l):
        res=l[0]
        for i in range(1,len(l)):
            res=res/l[i]
        return res
query=int(input())
for i in range(0,query):
    l=[i for i in input().split()]
    list=l[1:]
    c=calculator()
    for i in range(0,len(list)):
        list[i]=int(list[i])
    if(l[0]=="Add"):
        print(c.add(list))
    elif(l[0]=="Multiply"):
        print(c.multiply(list))
    elif(l[0]=="Divide"):
        print(int(c.divide(list)))
    elif(l[0]=="Subtract"):
        print(int(c.subtract(list)))
            