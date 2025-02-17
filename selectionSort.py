
def selection_Sort(my_List):
    n=len(my_List)#5
    for i in range(n):
        min_Index=i #0
        for j in range(i+1,n):
            if my_List[j]<my_List[min_Index]:
                min_Index=j#4 index
        my_List[i],my_List[min_Index]=my_List[min_Index],my_List[i] 
        
list1=[56,10 ,7 ,3 ,8 ,2,18]        
selection_Sort(list1)
print(list1)     

