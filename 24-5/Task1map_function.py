


def upper_1(upper1):
    return upper1.upper()
 
list1=["Saba","said","ali","DD"]
d1=list(map(lambda i: i.upper(),list1))
d2=list(map(upper_1,list1))
print(d1)
print(d2)
    