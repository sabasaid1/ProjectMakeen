def bainary(key):
    low=1
    high=key//2
    while(high >= low):
        mid =(high + low)//2
        if (mid*mid == key):
            return mid
        elif (mid*mid < key):
            low= mid + 1
        else:
            high= mid - 1
    return key 
        
            
        
        
x=int(input("enter number: "))
print(bainary(x))
