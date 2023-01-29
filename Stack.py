import collections

class Stack:
    def __init__(self):
        self.stk = collections.deque()
        self.size = 0
    
    def is_empty(self):
        if(self.size == 0):
            return True
        else:
            return False
            
    def peek(self):
        if (self.size <= 0):
            print("Empty stack")
        else:
            print(self.stk[-1])
        
    def push(self,data):
        self.stk.append(data)
        self.size+=1
    
    def pop(self):
        if self.size <= 0:
            print("Empty stack")
        else:
            self.stk.pop()
            self.size-=1
    
    def search(self,data):
        temp = 0
        while(temp < self.size):
            if (self.stk[temp] == data):
                print("Index of searched item = " + str(temp))
                return
            temp+=1
        print("Item not found")
    
    def __str__(self):
        print(self.stk)

