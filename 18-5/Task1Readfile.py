input_file = open("car.txt","r")
#time = input_file.readline()

'''for i in range(int(time)):
    print(input_file.readline())
input_file.close()'''
speed =0

for line in input_file:
    
    car1= line.split()
    print(car1)
    #car.append(int(car1))
    speed = int(car1[1]) * int(car1[0])
    
    print("The distance:" , speed)
    









