Year = int(input("input year:"))
 
if( (Year % 4 == 0) and (Year % 100 != 0)  or (Year % 400 == 0)):   
    print("Year:" ,Year," is a leap Year");   
else:  
     print ("Year:" ,Year," is not a leap Year")