

number = int(input("Enter number: "))
length=int(input("Enter length: "))
def multiples(number,length):
   
    print("The multiples are: ")
    for i in range(1,1+length):
        print(number*i, end =" ")
        

multiples(number,length)