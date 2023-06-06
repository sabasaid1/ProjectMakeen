

#Discount(1100,50)
#the price after Discount is 550
#Discount(130,30)
#the price after Discount is 91



price=int(input("enter price:"))
Discount=int(input("enter a Discount %:"))

def After_Discount(price,Discount):
    
    dis=price*Discount/100
    After_Discount=price-dis

    print("the price after Discount is " ,After_Discount)
    
    
After_Discount(price,Discount)