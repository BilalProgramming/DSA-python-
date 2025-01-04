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
bst.insert(50)
bst.insert(30)
bst.insert(10)
bst.insert(40)
bst.insert(35)
bst.insert(45)
bst.insert(70)
bst.insert(60)
print(bst.search(300))


print("in order travsersal")
bst.display3(bst.root)