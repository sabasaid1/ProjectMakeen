'''x= lambda a : a*2
print(x(2))

x= lambda a,b : a+b
print(x(2,5))

x= lambda a=3,b=1 : a+b
print(x())'''
########

pepole=[{'name':"saba",'age':21},{'name':"Mary",'age':20}]
#x= lambda pepole : [{'name':"saba",'age':21},{'name':"Mary",'age':20}]
        
#print()
#x= lambda name,age:[{"ss",20},{"sd",22}]

pepole.sort(key=lambda x:x['age' ])
print(pepole)
#print(x)

