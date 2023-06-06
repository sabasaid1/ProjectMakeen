
#Oman 309501
#China 9562910

size=148940000
country=input("enter country: ")
def world_land(country,size):
    
    
    size_area=int(input("enter a size: "))
    area=size_area/size*100

    print(country," occupies ",round(area, 2), "% of the total world land")
    
world_land(country,size)



