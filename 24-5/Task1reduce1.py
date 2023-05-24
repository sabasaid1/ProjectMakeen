#def reduce(upper1):
    #return upper1.upper()
from functools import reduce
list1=[2,2]
d1=reduce(lambda i,y : i+y**2 ,list1,0)
#d2=list(map(upper_1,list1))
print(d1)
#print(d2)