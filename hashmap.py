class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    
    def get_hash(self,key):
        h=0
        for char in key:
         h+=ord(char)
         return h%self.max
    def __setitem__(self,key,value):
        h=self.get_hash(key)     
        found=False
        for idx,elem in enumerate(self.arr[h]):
            # if key already exist
            if len(elem)==2 and elem[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break
        if not found: 
        # when no key exist on a patriculindex
          self.arr[h].append((key,value))#tuple
    def __getitem__(self,key):
        h=self.get_hash(key)
        for elem in  self.arr[h]:
            if elem[0]==key:
             return elem[1]
    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,elem in enumerate(self.arr[h]):
            if elem[0]==key:
                del self.arr[h][index]
    
               
        
            
h1=HashTable()
print(h1)
h1["jan 1"]=27
h1["jan 2"]=31
print(h1.arr)