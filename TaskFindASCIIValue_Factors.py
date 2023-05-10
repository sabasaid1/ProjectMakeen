###### Find ASCII Value of a Character

h="Hello"
### ord() function, which is a built-in function in Python that accepts a char (string of length 1)
print("Find ASCII Value of a Character ", ord(h[0]),ord(h[1]),ord(h[2]),ord(h[3]),ord(h[4]))

i=0
while(i < len(h)):
    print("The ASCII Value of Character %c = %d" %(h[i], ord(h[i])))
    i = i + 1

###find the factors

num=int(input("Enter the number: "))

print("\n the Factors of", num)
i = 1
while i<=num:
    if num%i==0:
        print(i)
    i = i+1
    

