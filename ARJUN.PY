import math


def mtrx_mul(b,a):
    s=[]
    for i in range(0,len(a)):
        l=[]
        for j in range(len(b[i])):
            row=0
            col=0
            sum=0
            while(row<len(a)):
                sum+=a[i][col]*b[row][j]
                row+=1
                col+=1
            l.append(sum)
        s.append(l)
    return s
                
def scaling(sx,sy,sz,matrix):
    s_matrix=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    k=mtrx_mul(matrix,s_matrix)

    return k

def translating(tx,ty,tz,matrix):
    t_matrix=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    k=mtrx_mul(matrix,t_matrix)

    return k

def rotation(AOR,angle,matrix):
    radian=((22/7)*angle)/180
    sin=math.sin(radian)
    cos=math.cos(radian)

    if AOR=="z":
        r_matrix=[[cos,-sin,0,0],[sin,cos,0,0],[0,0,1,0],[0,0,0,1]]
        
    elif AOR=="x":
        r_matrix=[[1,0,0,0],[0,cos,-sin,0],[0,sin,cos,0],[0,0,0,1]]
       
    elif AOR=="y":
        r_matrix=[[cos,0,sin,0],[0,1,0,0],[-sin,0,cos,0],[0,0,0,1]]
    
    k=mtrx_mul(matrix,r_matrix)

    return k



#main


n=int(input("enter the no. of vertices : "))
x,y,z,t=[],[],[],[]

j=input("enter for x: ").split()
for i in j:
    x.append(float(i))

k=input("enter for y: ").split()
for i in k:
    y.append(float(i))

l=input("enter for z: ").split()
for i in l:
    z.append(float(i))

for i in range(n):
    t.append(1)

matrix=[x,y,z,t]


with open("Matrix.txt","w") as f:
    f.write(str(x)+"\n"+str(y)+"\n"+str(z)+"\n")
g=0
while g==0:
    trans_no=int(input("enter the no. of transformations: "))
    for i in range(0,trans_no):
        q=input("enter the query: ").split()

        if q[0] in {"s","S"}:
            mtrx=scaling(float(q[1]),float(q[2]),float(q[3]),matrix)
            g=1

        elif q[0] in {"t","T"}:
            mtrx=translating(float(q[1]),float(q[2]),float(q[3]),matrix)
            g=1
        
        elif q[0] in {"r","R"}:
            if q[1] not in {"x","y","z"}:
                print("wrong axis of rotation. please try again  ")
            else:
                mtrx=rotation(q[1],float(q[2]),matrix)
                g=1
        else:
            print("Wrong input. please try again")



x=mtrx[0]
y=mtrx[1]
z=mtrx[2]

print(" x' = ",x,'\n',"y' = ",y,'\n',"z' = ",z)

with open("Matrix.txt","a") as f:
    f.write("matrix after conversion : ")
    f.write(str(mtrx))