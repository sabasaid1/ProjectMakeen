file = open("factor.txt","r")
for line in file:
    
    num= line.split()
    print(num)
    
    i = 1
    while i<=int(num[0]):
        if int(num[0])%i==0:
            print(i)
        i = i+1