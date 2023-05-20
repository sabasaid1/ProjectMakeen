arr=[2,6,1,9]
#print(arr[:2])
sum_1 = sum(arr)
target_sum = sum_1 / 2
r_sum=0
d=[]
for i in range(len(arr)):
    r_sum+=arr[i]
    #print(r_sum)
    if r_sum == target_sum :
       print(arr[:i+1], arr[i+1:])
       
print()