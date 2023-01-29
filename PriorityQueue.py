class PriorityQueueWithMinHeap:
    
    def __init__(self):
        self.heap = []
        
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    def clear(self):
        self.heap.clear()
    
    def peek(self):
        return self.heap[0]
    
    def index(self, data):
        for i in range(self.size()):
            if self.heap[i] == data:
                return i
        return False
    
    def add(self,data):
        if(data == None):
            print("Element value cannot be null")
        else:
            self.heap.append(data)
            last_index = self.size() - 1
            self.bubble_up(last_index)
    
    def poll(self):
        return self.remove_at(0)
    
    def remove_element(self, data):
        i = self.index(data)
        if(i is not False):
            return self.remove_at(i)
            
    def remove_at(self, index):
        if(self.size() == 0):
            return None
        last_index = self.size() - 1
        self.swap(index, last_index)
        removed_data = self.heap.pop()
        element = self.heap[index]
        
        self.bubble_down(index)
        if (self.heap[index] == element):
            self.bubble_up(index)
         
        return removed_data
        
        
    def bubble_up(self, elem_index):
        while(True):
            parent_index = (elem_index - 1)//2
            if(parent_index < 0): 
                break
            if(self.greater(parent_index, elem_index)):
                self.swap(parent_index, elem_index)
                elem_index = parent_index
            else:
                break
            
    def bubble_down(self, elem_index):
        size = self.size()
        while(True):
            left = elem_index*2 + 1
            right = elem_index*2 + 2
            smallest = left
            if(right < size and self.greater(left,right)):
                smallest = right
            if(left >= size or self.greater(left, elem_index)):
                break
            self.swap(elem_index, smallest)
            element_index = smallest
            
    def greater(self, index1, index2):
        if(self.heap[index1] > self.heap[index2]):
            return True
        else:
            return False
    
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
        
    def __str__(self):
        print(self.heap)
        


            
            