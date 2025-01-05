class Queue:
    def __init__(self):
        self.queue=[]
        print("queue is created...")
        
    def endQueue(self,item):
        self.queue.append(item)
        
    def deQueue(self):
        if self.is_Empty():
            raise IndexError("queue underFlow")
            return None
        return self.queue.pop(0)
        
    def is_Empty(self):
        return len(self.queue)==0
        
    def get_Front(self):
        if self.is_Empty():
            raise IndexError("queue underFlow")
            return None
        return self.queue[0]
        
    def get_Rear(self):
        if self.is_Empty():
            raise IndexError("queue underFlow")
            return None
        return self.queue[-1]
        
    def size(self):
            return len(self.queue)
            
q1=Queue()
try:
 print(q1.get_Front())
except IndexError as e:
 print(e.args[0])
q1.endQueue(5)
q1.endQueue(10)
q1.endQueue(15)
q1.endQueue(20)
try:
 print("Front=: ",q1.get_Front(),"Rear=: ",q1.get_Rear())
except IndexError as e:
    print(e.args[0])
try:
 print("deque: ",q1.deQueue())
 print(q1.size())
except IndexError as e:
 print(e.args[0])