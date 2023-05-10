y = input("word :")


mid= len(y)//2


if (len(y) % 2 != 0) :
   print(y[mid])
   
else :
   print(y[mid-1],y[mid])
