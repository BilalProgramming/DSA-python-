def quick_Sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]   
        greater=[x for x in list1[1:] if x>pivot] 
        return quick_Sort(lesser)+[pivot]+quick_Sort(greater)
        
l1=[  5,1,1,2,0,0 ]
l1=quick_Sort(l1)    
print(l1)

