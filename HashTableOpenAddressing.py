class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)
        
class HashTableOpenAddressing:
    
    def __init__(self, capacity, max_load_factor):
        if(capacity < 0): raise Exception("Give a capacity greater than 0")
        if(max_load_factor<=0 or max_load_factor == None): raise Exception("Illegal load factor")
        self.capacity = capacity
        self.max_load_factor = max_load_factor
        self.threshold = capacity * max_load_factor
        self.ht = [None] * capacity
        self.size = 0
        self.initial_tombstone_index = None
        
    def clear(self):
        self.ht.clear()
        self.size = 0
    
    def length(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def normalize_index(self,hash):
        return abs(hash) % self.capacity
        
    def seek_entry(self,hash_value, key):
        if(key == None): return None
        size = self.capacity
        for i in range(size*2):
            new_index = (hash_value + i) % size # a = 1
            if(self.ht[new_index] != None and self.ht[new_index] != 'Tombstone' and self.ht[new_index].key == key):
                return new_index
            elif(self.ht[new_index] == 'Tombstone'):
                self.initial_tombstone_index = new_index
        return None
    
    def has_key(self,key):
        bucket_index = self.normalize_index(hash(key))
        print(self.seek_entry(bucket_index,key) != None)
        
    def seek_empty_slot(self,hash_value):
        size = self.capacity
        for i in range(size*2):
            new_index = (hash_value + i) % size # a = 1
            if(self.ht[new_index] == None or self.ht[new_index] == 'Tombstone'):
                return new_index
        
    def resize_table(self):
        self.capacity = self.capacity * 2
        self.threshold = self.capacity * self.max_load_factor
        new_ht = [None] * self.capacity
        table = self.ht
        
        for i in range(len(table)):
            bucket = table[i]
            if(bucket != None and bucket != 'Tombstone'):
                index = self.normalize_index(bucket.hash)
                if(new_ht[index] != None):
                    index = self.seek_empty_slot(index)
                new_ht[index] = bucket
                
        self.ht.clear()
        self.ht = new_ht
    
        
    def add_pairs(self, key, value):
        if(key == None): print("Key cannot be null")
        else:
            new_entry = Entry(key, value)
            index = self.normalize_index(new_entry.hash)
            if(self.ht[index] != None):
                index = self.seek_empty_slot(index)
            self.ht[index] = new_entry
            self.size+=1
            if (self.size > self.threshold):
                self.resize_table()
            
                
    
    def lookup(self, key):
        if(key == None): 
            print("Key cannot be null")
            return
        hash_value = self.normalize_index(hash(key))
        index = self.seek_entry(hash_value,key) 
        if(index != None):
            print(self.ht[index].value)
            if(self.initial_tombstone_index != None):
                self.ht[self.initial_tombstone_index] = self.ht[index]
                self.ht[index] = None
                self.initial_tombstone_index = None
        else:
            print("Key-value pair not found")
        
  
    def removal(self, key):
        if(key == None): print("Key cannot be null")
        else:
            hash_value = self.normalize_index(hash(key))
            index = self.seek_entry(hash_value, key)
            if(index != None):
                self.ht[index] = 'Tombstone'
            else:
                print("key does not exist")
    
                
    def __str__(self):
        table = self.ht
        for i in range(len(table)):
            bucket = table[i]
            if(bucket != None and bucket != 'Tombstone'):
                print(i, bucket.key, bucket.value)
            else:
                print(i, bucket)
            