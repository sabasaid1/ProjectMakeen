file = open("memory.txt","r")
data1=[]
m1 =[]
m2=[]
for line in file:
    data = line.split()
    data1.append(data)
#print(data1)
m1.append(data1[0])
m2.append(data1[1])



#Memory size

for i in m1:
    
    size = int(i[1]) * int(i[2])
#print(size)

    if int(i[0]) > size:
        print(i," Yes")
    else:
        print(i ," No")

for i in m2:
    
    size = int(i[1]) * int(i[2])
#print(size)

    if int(i[0]) > size:
        print(i, "Yes")
    else:
        print(i ,"No")

