class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)
        
class HashTableSeparateChaining:
    
    def __init__(self, capacity, max_load_factor):
        if(capacity < 0): raise Exception("Give a capacity greater than 0")
        if(max_load_factor<=0 or max_load_factor == None): raise Exception("Illegal load factor")
        self.capacity = capacity
        self.max_load_factor = max_load_factor
        self.threshold = capacity * max_load_factor
        self.ht = [[] for x in range(capacity)]
        self.size = 0
        
    def clear(self):
        self.ht.clear()
        self.size = 0
    
    def length(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def normalize_index(self,hash):
        return abs(hash) % self.capacity
        
    def bucket_seek_entry(self,bucket_index, key):
        if(key == None): return None
        bucket = self.ht[bucket_index]
        if len(bucket) == 0: return None
        for i in bucket:
            if(i.key == key):
                return i
        return None
    
    def has_key(self,key):
        bucket_index = self.normalize_index(hash(key))
        print(self.bucket_seek_entry(bucket_index,key) != None)
        
    def resize_table(self):
        self.capacity = self.capacity * 2
        self.threshold = self.capacity * self.max_load_factor
        new_ht = [[] for x in range(self.capacity)]
        table = self.ht
        
        for i in range(len(table)):
            bucket = table[i]
            if(bucket != []):
                for j in range(len(bucket)):
                    bucket_index = self.normalize_index(bucket[j].hash)
                    new_ht[bucket_index].append(bucket[j])
                    
        self.ht.clear()
        self.ht = new_ht
    
    
    def bucket_insert_entry(self, bucket_index, new_entry):
        bucket = self.ht[bucket_index]
        if(self.bucket_seek_entry(bucket_index,new_entry.key) == None):
            bucket.append(new_entry)
            self.size+=1
            if (self.size > self.threshold):
                self.resize_table()
        
    def add_pairs(self, key, value):
        if(key == None): print("Key cannot be null")
        else:
            new_entry = Entry(key, value)
            bucket_index = self.normalize_index(new_entry.hash)
            self.bucket_insert_entry(bucket_index, new_entry)
            
    def lookup(self, key):
        if(key == None): 
            print("Key cannot be null")
            return
        bucket_index = self.normalize_index(hash(key))
        bucket = self.ht[bucket_index]
        if len(bucket) == 0: 
            print("Key-value pair not found")
            return
        for i in bucket:
            if(i.key == key):
                print(i.value)
                return
        print("Key-value pair not found")
        
    def bucket_remove_entry(self,bucket_index, key):
        bucket = self.ht[bucket_index]
        if bucket == []: 
            print("key does not exist")
            return
        for i in range(len(bucket)):
            if (bucket[i].key == key):
                bucket.pop(i)
                self.size-=1
                return
        print("key does not exist")
        
    def removal(self, key):
        if(key == None): print("Key cannot be null")
        else:
            bucket_index = self.normalize_index(hash(key))
            self.bucket_remove_entry(bucket_index, key)
        
    def __str__(self):
        table = self.ht
        for i in range(len(table)):
            bucket = table[i]
            if(bucket == []):
                print("Key-value pairs at index " + str(i), bucket)
            else:
                print("Key-value pairs at index " + str(i))
                for j in range(len(bucket)):
                    print(j, bucket[j].key, bucket[j].value)