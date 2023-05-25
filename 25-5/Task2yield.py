


nums=[1,2,3,4,6,8]
def even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num 
        

value=even(nums)
for i in value:
    print(i)
    
'''    
def even(nums):
    for num in range(16):
        if num % 2 == 0:
            yield num 
        

value=even(16)
for i in value:
    print("i:",i)

''' 
