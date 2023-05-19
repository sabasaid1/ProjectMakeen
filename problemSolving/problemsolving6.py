arr =[1,2,3,4,5]

#for i in arr:
    
    #i[] -= l
    #print(i,end=" ")
list_1 =[]
#list_1 = [arr[(i + 2) % len(arr)]
#print(list_1)
#for i, x in enumerate(arr)]:
    
    #print ("Output of the list after left rotate by 3 : " + str(list_1))
          
for i in arr:
    left_rotate=2
    list_1 = arr[left_rotate:] + arr[:left_rotate]

print ("Output of the list after left rotate by 2 : " + str(list_1))