'''
output
1 0 0 0 
2 1 0 0 
2 2 1 0 
2 2 2 1
'''


c=[]



for i in range(4):
    a=[]
    for j in range(4):
        if [i]==[j]:
            a.append(1)
        if [i]>[j]:
            a.append(2)
        if [i]<[j]:
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