
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if (num1 == num2) and (num1 == num3):
   print("The number are equal")
elif (num1 >= num2) and (num1 >= num3):
   print(num1," is The largest")
elif (num2 >= num1) and (num2 >= num3):
   print(num2," is The largest")
else :
   print(num3," is The largest")



