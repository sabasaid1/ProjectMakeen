file = open("greatest_common_divisor.txt","r")
data1=[]

d1=[]
d2=[]
d3=[]

for line in file:
    data=line.split()
    data1.append(data)
print(data1)
d1.append(data1[0])
d2.append(data1[1])
d3.append(data1[2])
#print(d1)
#print(d2)
#print(d3)


import math
for i in d1:
    
    x=math.gcd(int(i[0]),int(i[1]))
    print("greatest common divisor in ",int(i[0]),int(i[1]),"is: ",x)
    

for i in d2:
    
    x=math.gcd(int(i[0]),int(i[1]))
    print("greatest common divisor in ",int(i[0]),int(i[1]),"is: ",x)
    

for i in d3:
    
    x=math.gcd(int(i[0]),int(i[1]))
    print("greatest common divisor in ",int(i[0]),int(i[1]),"is: ",x)
    
