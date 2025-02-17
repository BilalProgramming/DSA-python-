def bubbleSort(list_data):
     
     for i in range(1,len(list_data)):
         for j in range(len(list_data)-i):
             if list_data[j]>list_data[j+1]:
                 list_data[j],list_data[j+1]=list_data[j+1],list_data[j]
                 
list=[18,17,9,5,15,0,-8]            
bubbleSort(list)         
print(list)   
