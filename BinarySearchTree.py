import collections
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node_count = 0
        
    def length(self):
        return self.node_count
    
    def is_empty(self):
        return self.node_count == 0
        
    def find_recursive(self,data,temp):
        if(temp == None):
            return False
        elif(data < temp.data):
            return self.find_recursive(data,temp.left)
        elif(data > temp.data):
            return self.find_recursive(data,temp.right)
        elif(data == temp.data):
            return True
        
    def contains(self,data):
        if(data == None): raise Exception("Data in a node cannot be null")
        if self.find_recursive(data,self.root) == True:
            print("Node exists")
        else:
            print("Node does not exist")

    def add_recursive(self,data,temp):
        if(temp == None):
            return Node(data)
        elif(data < temp.data):
            temp.left = self.add_recursive(data,temp.left)
        elif(data > temp.data):
            temp.right = self.add_recursive(data,temp.right)
        elif(data == temp.data):
            return temp
        
    def add(self, data):
        if(data == None): raise Exception("Data in a node cannot be null")
        if(self.find_recursive(data,self.root) != True):
            if(self.root == None): self.root = Node(data)
            else:
                self.add_recursive(data,self.root)
                self.node_count+=1
        
    def find_min(self,temp):
        while(temp.left != None): temp = temp.left
        return temp
        
    def remove_recursive(self,data,temp):
        if(temp == None):
            return None
        elif(data < temp.data):
            temp.left = self.remove_recursive(data,temp.left)
        elif(data > temp.data):
            temp.right = self.remove_recursive(data,temp.right)
        elif(data == temp.data):
            if(temp.right == None):
                return temp.left
            elif(temp.left == None):
                return temp.right
            else:
                lowest_node = self.find_min(temp.right)
                temp.data = lowest_node.data
                temp.right = self.remove_recursive(lowest_node.data, temp.right)
        
    def remove(self, data):
        if(data == None): raise Exception("Data in a node cannot be null")
        if(self.find_recursive(data,self.root) == True):
            self.node_count-=1
            self.remove_recursive(data,self.root)
            
    def height_recursive(self,temp):
        if(temp == None): return 0
        return max(self.height_recursive(temp.left),self.height_recursive(temp.right)) + 1
        
    def height(self):
        height = self.height_recursive(self.root)
        print("Height - " + str(height))
        
   # def in_order_traversal(self):
        
        
   # def pre_order_traversal(self):
        
        
   # def post_order_traversal(self):
        
        
    def level_order_traversal(self):
        Queue = collections.deque()
        Queue.append(self.root)
        print_list = []
        while(bool(Queue) != False):
            elem = Queue.popleft()
            if(elem.left != None):
                Queue.append(elem.left)
            if(elem.right != None):
                Queue.append(elem.right)
            print_list.append(elem.data)
        print(print_list)
        
