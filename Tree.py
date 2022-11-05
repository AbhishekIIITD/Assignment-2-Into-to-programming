class treeNode:
    def __init__(self,data):
        self.data=data
        self.childrens=[]
def treeInput():
    root=int(input())
    root=treeNode(root)
    childrens=int(input("Enter number of childrens :"))
    for i in range(0,childrens):
        child=treeInput()
        root.childrens.append(child)
    return root
def printTree(root):
    print(root.data)
    for i in range(0,len(root.childrens)):
        printTree(root.childrens[i])
    

root=treeInput()

printTree(root)