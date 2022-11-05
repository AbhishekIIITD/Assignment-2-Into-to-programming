def normaltraverse(l):
    li=[]
    length=len(l)
    for i in range(0,length):
        for j in range(0,length):
            li.append(l[i][j])
    return li

def alternatetraverse(l):
    li=[]
    length=len(l)
    for i in range(0,length):
        if(i%2!=0):
            j=length-1
            while(j>=0):
                li.append(l[i][j])
                j-=1
        else:
            for j in range(0,length):
                li.append(l[i][j])
    return li
def boundarytraversal(l,topr,btnr,leftc,rightc):
    
    li=[]
    i=topr
    j=leftc
    
    while(j<rightc):
        li.append(l[i][j])
        j+=1
    topr+=1
    while(i<btnr):
        li.append(l[i][j])
        i+=1
    rightc-=1
    while(j>leftc):
        li.append(l[i][j])
        j-=1
    btnr-=1
    while(i>=topr):
        li.append(l[i][j])
        i-=1

    leftc+=1
    return li


def spiraltraversal(l,topr,btmr,leftc,rightc,output):
    if(topr>btmr or leftc>rightc):
        return
    small=boundarytraversal(l,topr,btmr,leftc,rightc)
    output.extend(small)
    return spiraltraversal(l,topr+1,btmr-1,leftc+1,rightc-1,output)


def diagonaltraversalRL(l):

    li=[]
    n=len(l)
    i=0
    j=0
    while(j<n):
        i=0
        k=j

        while(k>=0):
            li.append(l[i][k])
            k=k-1
            i+=1
        j+=1
    i=1
    j=n-1
    while(i<n):
        j=n-1
        k=i
        while(j>=i):
            li.append(l[k][j])
            k+=1
            j-=1
        i+=1


    return li

def diagnoltraversalLR(l):
    li=[]
    n=len(l)
    i=0
    j=len(l)-1
    while(j>=0):
        i=0
        k=j

        while(k<n):
            li.append(l[i][k])
            k=k+1
            i+=1
        j-=1
    i=1
    while(i<n):
        j=0
        k=i
        while(k<n):
            li.append(l[k][j])
            k+=1
            j+=1
        i+=1


    return li
l=[[1,2,3],[4,5,6],[7,8,9]]