

import re
password = input("Enter a password: ")
f = True
while True:
        
        if len(password) < 8:
            f=False
            break
        elif not re.search('[0-9]',password):
            f=False
            break
        elif not re.search('[A-Z]',password) :
            f=False
            break
        elif not re.search('[a-z]',password) :
            f=False
            break
        elif not re.search('[-@$]',password) :
            f=False
            break
        else:
            print("the password is vaild")
            break
        
if f == False:
    print("password is not vaild")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
length = lower = upper = digit = Sym = False

password = input('Enter the password: ')
Sym =['$', '@', '#', '%']
if len(password) >= 8:
    length = True
    
    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
        elif char in Sym:
            Sym = True


if length and lower and upper and digit:
    print('That is a valid password.')
else:
    print('That password is not valid.')


val = True
'''
#l = len(p) >= 8
Sym =['$', '@', '#', '%']
'''
if len(p) >= 8:
    for char in p:
        if char.isdigit():
            val=False
        elif cahr.isupper():
            val = False
        elif cahr.isupper():
            val = False
        elif cahr == sym:
            val = False
            
            
if val:
    print("valid")
else:
    print("not vaild")'''



