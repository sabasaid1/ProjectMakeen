'''list1=[2,4,5,6,7,9,10]
l1=list1.index(min(list1))
h1=list1.index(max(list1))
mid = (h1+l1)//2
print(mid)
print(l1)
print(h1)
key=5
for i in list1:
    if i[mid] == key:
        print(mid)
    elif key < i[mid]:
        
'''      
def nbinar(mylist,key):
    low=0
    high=len(mylist)-1
    while(high >= low):
        mid =(high + low)//2
        if (mylist[mid] == key):
            return mid
        elif (mylist[mid] > key):
            low= mid + 1
        else:
            high= mid-1
    return key 
        
            
        
        
mylist=[1,2,3,4,5,9]
print(nbinar(mylist,3))



