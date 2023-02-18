#Queue Data Structure Implemented using Deque in Python
import collections

class Queue:
    def __init__(self):
        self.que = collections.deque()
        self.size = 0
    
    def is_empty(self):
        if(self.size == 0):
            return True
        else:
            return False
    
    def length(self):
        return self.size
            
    def peek(self):
        if (self.size <= 0):
            print("Empty queue")
        else:
            print(self.que[-1])
        
    def enqueue(self,data):
        self.que.append(data)
        self.size+=1
    
    def dequeue(self):
        if self.size <= 0:
            print("Empty queue")
        else:
            self.que.popleft()
            self.size-=1
    
    def __str__(self):
        print(self.que)

