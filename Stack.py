class stack:
    def __init__(self,data):
        self.data=[]
        self.data.append(data)
        self.size=1
    def isEmpty(self):
        if(self.size==0):
            return True
    def push(self,data):
        self.data.append(data)
        self.size+=1
    def pop(self):

        if(self.size==0):
            return "stack is empty"
        x=self.data.pop()
        self.size-=1
        return x
    def top(self):
        if(self.isEmpty()):
            return "Stack is Empty"
        return self.data[self.size-1]
