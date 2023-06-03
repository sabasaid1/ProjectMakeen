lst = [[1,2,3],
       [4,5,6],
       [9,8,9]]

for i in range(3):
    for j in range(3):
        print(lst[i][j],end='  ')
        
    print()
c=[]

for i in range(3):
    
    r1=[]
    l1=[]
    m1=[]
    
    for j in range(3):
        if lst[i]==lst[j]:
            s = lst[i][j]

        if lst[i]==lst[j]:
            m = lst[1][1]
        if lst[i]<=lst[j]:
            r = lst[0][2]
        if lst[i]>=lst[j]:
            l = lst[2][0]
            
            
            
    c.append(s)
    m1.append(m)
    r1.append(r)
    l1.append(l)
    #print(s)
    #print(l)
sum_num=sum(c)
print(sum_num)
sum_num1= m1 + r1 + l1
print(sum(sum_num1))
subtraction_num =int(sum_num) - sum(sum_num1)
print(abs(subtraction_num))