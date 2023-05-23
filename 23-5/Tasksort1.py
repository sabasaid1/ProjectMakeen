def insertsort(array):
    for step in range(1,len(array)):
        key=array[step]
        j=step -1
        while j >= 0 and key < array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1] =key
        
        
array=[3,5,10,1,2]
insertsort(array)
print(array)

for i in range(len(array)):
    print(array[i] ,end=" ")