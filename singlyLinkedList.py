
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:     
    def __init__(self,start=None):
        self.start=start
        
    def is_Empty(self):
        return self.start==None
            
    def insert_At_Start(self,data):   
         n=Node(data,self.start)
         self.start=n
    def insert_At_Last(self,data):
        n=Node(data)    
        if not self.is_Empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
         self.start=n        
         
    def search(self,data):
         temp=self.start
         while temp is not None:
             if temp.item==data:
              return temp
             temp=temp.next
         return None    
         
    def insert_After(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            
    def delete_First(self):
        if self.start is not None:
            self.start=self.start.next
            
    def delete_Last(self):
        if self.start is None: 
            pass
        elif self.start.next is None:
            self.start=None    
        else:  
            temp=self.start
            while  temp.next.next is not None:
                temp=temp.next
            temp.next=None
            
                     
            
    
            
    def delete_Item(self,data):
         if self.start is None:
             pass
             
         elif self.start.next is None:
             if self.start.item==data:
                 self.start=None
                 
         else:
             temp=self.start
             if temp.item==data:
                 self.start=temp.next
             else:
                 while temp.next is not None:
                     if temp.next.item==data:
                         temp.next=temp.next.next
                         break
                     temp=temp.next    
                            
                 
                       
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next           
                       
myList=SLL()      
print("SLL is Empty?",myList.is_Empty()) 
myList.insert_At_Start(4)
myList.insert_At_Start(8)
myList.insert_At_Last(20)
myList.display()# 8  4 20
myList.delete_Item(4)
print()
myList.display()
print()
print(myList.search(200))

