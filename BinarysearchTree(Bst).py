#implement bst
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
class BST:
    def __init__(self):        
        self.root=None
        
    def insert(self,item):
        self.root=self.rinsert(self.root,item)#recussively call
        
    def rinsert(self,root,data):
        if root is None:  # if empty
            return Node(data)
        elif data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
        return root        
    def search(self,data):
        node=self.rsearch(self.root,data) #recursively call 
        return node
    def rsearch(self,root,data):
        if root is None or root.item==data:#check for empty or 1st node isequal to data
            return root    
        elif data<root.item:#if data is less than root then search in left sub tree
            return self.rsearch(root.left,data)
        elif data>root.item:#if  data is greater than root then search in right sub tree
            return self.rsearch(root.right,data)
        
    def min_value(self,root):
            current=root
            while current.left is not None:
                current=current.left
            return current.item    
    
    def max_value(self,root):
            current=root
            while current.right is not None:
                current=current.right
            return current.item    
    
    def delete(self,data):#delete function
        self.root=self.rdelete(self.root,data)  #rdelete check recursively for each node  
    def rdelete(self,root,data):
        if root is None:
            return root
        elif data<root.item:
           root.left=self.rdelete(root.left,data)
        elif data>root.item:
            root.right=self.rdelete(root.right,data) 
        #if root.item is equal to data then check 3 cases (1) if no child,(2) only one child,(3) two child
        else: 
            if root.left is None:
             return root.right
            elif root.right is None:
             return root.left
            else:#if two child exist then i choose greater elements of left subtree
             root.item=self.max_value(root.left)
             root.left=self.rdelete(root.left,root.item)
        return root

               
            #Preorder Traversal    
    def display1(self,root):
        if root is None:
            return None
        else: 
           temp=root
           print(temp.item)  
           self.display1(temp.left)
           self.display1(temp.right)      
    #post order travsersal       
    def display2(self,root):
        if root is None:
            return None
        else:
            temp=root
            self.display2(temp.left)
            self.display2(temp.right)
            print(temp.item)    
    #in order traversal
    def display3(self,root):
        if root is None:
            return None
        else:
            temp=root
            self.display3(temp.left)
            print(temp.item)
            self.display3(temp.right)
                                        
bst=BST()  # root=None
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)

print("In-order traversal before deletion:")
bst.display3(bst.root)

bst.delete(6)

print("In-order traversal after deletion: 6 ")
bst.display3(bst.root)
