
#Q2

import math
n=int(input("num of side"))
s=float(input("enter side"))
def area(n,s):
    area1 = (n*s**2)/(4*math.tan(3.14/n))  ## math.pi
    return area1
    
print("area:",area(n,s))



#Q3

s=input("enter:").lower()
def coutVowels(s):
    c=0
    v=['a','i','e','o','u']
    for i in s:
        if i in v:
            c=c+1
    return c
            
print(coutVowels(s))
'''
s="Saaaaiss"
v=['a','i','e','o','u']
c=0

for i in s:
    if i in v:
        c=c+1
    elif i.isupper():
        c=c+1
        
print(c)
'''
    
    
    



