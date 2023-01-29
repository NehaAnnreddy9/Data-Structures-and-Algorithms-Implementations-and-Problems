#Doubly Linked List Implementation in Python
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
        
class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
   
    def __str__(self):
        if self.size == 0:
            print("Empty list")
            return
        trav = self.head
        while(trav != None):
            print(trav.data)
            trav = trav.next
    
    def clear(self):
        if (self.size == 0): 
            print("Linked list is empty")
            return
        trav = self.head
        while(trav != None):
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next
        self.head = self.tail = trav = None
        self.size = 0
            
            
    def length(self):
        return self.size
    
    def is_empty(self):
        if(self.length() == 0):
            return True
        else:
            return False
    
    def add_at_first(self,data):
        if (self.size == 0):
            new_node = Node(data,None,None)
            self.head = self.tail = new_node
        else:
            new_node = Node(data,None,self.head)
            self.head.prev = new_node
            self.head = new_node
        self.size = self.size + 1
            
    
    def add_at_last(self,data):
        if (self.size == 0):
            new_node = Node(data,None,None)
            self.head = self.tail = new_node
        else:
            new_node = Node(data,self.tail,None)
            self.tail.next = new_node
            self.tail = new_node
        self.size = self.size + 1
        
        
    def add_at_index(self, data, index):

        if (index == 0):
            self.add_at_first(data)
            return
        if (index == self.size):
            self.add_at_last(data)
            return
        
        trav = self.head
        trav_index = 0
        while(trav_index != index):
            trav = trav.next
            trav_index+=1
            
        new_node = Node(data,trav.prev,trav)
        trav.prev.next = new_node
        trav.prev = new_node
        self.size = self.size + 1
        
        
    def remove_at_first(self):
        if(self.length() == 0):
            print("Empty linked list")
            return 
        else:
            trav = self.head
            self.head = self.head.next
            trav.prev = trav.next = None
            trav.data = None
            self.size-= 1
    
    
    def remove_at_last(self):
        if(self.length() == 0):
            print("Empty linked list")
            return 
        else:
            trav = self.tail
            self.tail = self.tail.prev
            trav.prev = trav.next = None
            trav.data = None
            self.size-= 1
    
    
    def remove_at_index(self, index):
        if (index == 0):
            self.remove_at_first()
            return
        elif (index == self.size):
            self.remove_at_last()
            return
        
        trav = self.head
        trav_index = 0
        while(trav_index != index):
            trav = trav.next
            trav_index+=1
        
        trav.prev.next = trav.next
        trav.next.prev = trav.prev
        trav.prev = trav.next = None
        trav.data = None
        self.size-= 1
