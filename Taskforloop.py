'''
name = "Virgina"
for letter in name :
    print(letter , end = '')
'''  
##########
string = int(input("enter number"))
total = 0
count =0
for i in range(string + 1):
    if (string !=""):
        i = float(string)
        total = total + i
        count = count + 1
        string = input("enter number1")
    
        
if(count > 0):
    avg = total/count
    print(avg)
else:
    avg=0
    print(avg)

    
    

'''for i in range(string):
    total = total + i
    print(total)
print("ss")'''
        
        
        
    
    
