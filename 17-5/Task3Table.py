
'''
output
1 0 1 0 
0 1 0 1 
1 0 1 0 
0 1 0 1
'''
c=[]
for i in range(4):
    a=[]
    
    for j in range(4):
        r =i+j
        if (r % 2) == 0 :
            a.append(1)
        if (r % 2) != 0 :
            a.append(0)
        
    c.append(a)
    #print(c,end=' ')
        #print([[0]*3 for i in range(3)])
        
    #print()
    
for i in range(4):
    for j in range(4):
        print(c[i][j],end=' ')
        #print([[0]*3 for i in range(3)])
        
    print()