file=open("List.txt","r")
l1=[]
l2=[]
l3=[]
#t=file.readlines()
#print(t)


for line in file:
    data= line.split()
    #print(data)
    l1.append(data)

    
#print(l1)

for i in l1[0]:
    if l1[0].count(i) > 1:
            
        l2.append(i)

for i in l1[1]:
    if l1[1].count(i) > 1:
            
        l3.append(i)

print(l2,"the max:", max(l2))
print(l3, "the max:",max(l3))

#print(max(i))
        