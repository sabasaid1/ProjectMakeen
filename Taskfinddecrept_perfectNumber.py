'''

a=3
b=4
for i in range(a):
    for j in range(b):
        print("[]",end="")
    print()
''' 
############
'''str1 =("hello")

for i in str1:
    print(chr(ord(i) + 3),end="")
'''

str2 =("|rx#duh#juhdwh")

for i in str2:
    print(chr(ord(i) - 3),end="")
    
    
### find perfect number
print("\n")
sum = 0
t=0
num = int(input("num : "))
for i in range(1,num):
    if(num % i == 0):
        print(i,end =",")
        sum = sum + i
        #t = sum/2
print("\n")
if(sum == num):
   print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")


    

    
    
