#find cone_size Volume(7,4) output 117.22



r=int(input("enter r:"))
h=int(input("enter h:"))
def Volume(h,r):
    
    cone_size=1/3*3.14*r**2*h

    print("cone_size : ",round(cone_size, 2))
    
Volume(h,r)
    
    
    
