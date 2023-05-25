def fibonicci_num(nums):
    x,y=0,1
    for i in range(nums):
        x,y=y,x+y
        yield x
def squara(nums):
    for num in nums:
        yield num**2
        
def num3(nums):
    for num in nums:
        yield num**3
        
print(sum(num3(squara(fibonicci_num(10)))))
#print(num3(squara(fibonicci_num(10))))