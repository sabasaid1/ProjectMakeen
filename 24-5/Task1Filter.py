

#
def lowercase(i):
    return i.islower()
    



list1=["Saba","said","ali","DD"]
d1=list(filter(lambda i: i.islower(),list1))
d2=list(filter(lowercase,list1))
print(d1)
print(d2)
    
            
            