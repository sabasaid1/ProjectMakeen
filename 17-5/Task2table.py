

r=int(input("enter row:"))
c=int(input("enter column:" ))


#b = [[]*c for i in range(r)]
#print(b)
#print(b)
lst = []
for i in range(r):
    list2=[]
    for j in range(c):
        n=int(input("enter num:" ))
        list2.append(n)
    lst.append(list2)
    print(lst)
    
for i in range(r):
    for j in range(c):
        print(lst[i][j],end=' ')
        #print([[0]*3 for i in range(3)])
        
    print()


        