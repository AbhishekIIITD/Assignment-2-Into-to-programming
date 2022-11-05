import math 
def matrixmul(b,a):
    res=[]
    for i in range(0,len(a)):
        list=[]
        for j in range(len(b[i])):
            row=0
            col=0
            sum=0
            while(row<len(a)):
                sum=sum+a[i][col]*b[row][j]
                row+=1
                col+=1
            list.append(sum)
        res.append(list)
    return res
                
def Scaling(sx,sy,sz,x):
    scalingmatrix=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    return matrixmul(x,scalingmatrix)

def tranlating(tx,ty,tz,x):
    transmatrix=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    return matrixmul(x,transmatrix)

def rotation(angle,dir,matrix):
    radian=(math.pi*angle)/180
    sin=math.sin(radian)
    cos=math.cos(radian)
    #none
    if(dir=="x"):
        rotationmatrix=[[1,0,0,0],[0,cos,-sin,0],[0,sin,cos,0],[0,0,0,1]]
    elif(dir=="y"):
        rotationmatrix=[[cos,0,sin,0],[0,1,0,0],[-sin,0,cos,0],[0,0,0,1]]
    elif(dir=="z"):
        rotationmatrix=[[cos,-sin,0,0],[sin,cos,0,0],[0,0,1,0],[0,0,0,1]]
    else:
        return "wrong direction"
    return matrixmul(matrix,rotationmatrix)



    




vertices=int(input("Enter the no. of vertices : "))
x=[float(i) for i in input().split()]
y=[float(i) for i in input().split()]
z=[float(i) for i in input().split()]
t=[1 for i in range(0,vertices)]
matrix=[x,y,z,t]

with open("matrix.txt","w") as matrixf:
    matrixf.write(str(x)+"\n"+str(y)+"\n"+str(z)+"\n")


q=int(input("Enter the no. of transformations : "))
for i in range(0,q):
    query=input("Enter the query : ")
    query=query.split()

    if(query[0]=="S" or query[0]=="s"):
        matrix=Scaling(float(query[1]),float(query[2]),float(query[3]),matrix)
    elif(query[0]=="t" or query[0]=="T"):
        matrix=tranlating(float(query[1]),float(query[2]),float(query[3]),matrix)
    elif(query[0]=="r" or query[0]=="R"):
        matrix=rotation(float(query[2]),query[1],matrix)
    else:
        print("Wrong input")
x=matrix[0]
y=matrix[1]
z=matrix[2]
print("x' = ",x)
print("y' = ",y)
print("z' = ",z)
with open("matrix.txt","a") as matrixf:
    matrixf.write("Converted matrix is : ")
    matrixf.write(str(matrix))






