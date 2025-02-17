def merge_Sort(list1):
 if len(list1)<=1:   #base case for recusrsion
     return list1
 middle=len(list1)//2
 leftList=list1[:middle]
 rightList=list1[middle:]
 merge_Sort(leftList)
 merge_Sort(rightList)
 
 i=j=k=0
 while i<len(leftList) and j<len(rightList):
     if leftList[i]<rightList[j]:
         list1[k]=leftList[i]
         i+=1
     else:
         list1[k]=rightList[j]
         j+=1
     k+=1     
 while i<len(leftList):
     list1[k]=leftList[i]
     i+=1
     k+=1
 while j<len(rightList):
     list1[k]=rightList[j]
     j+=1
     k+=1
 return list1
l1=[75,29,83,42,16,90,56,34,20,71,88,92,7] 
merge_Sort(l1)
print(l1)

