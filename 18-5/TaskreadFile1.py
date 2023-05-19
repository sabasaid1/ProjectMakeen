input_file= open("file.txt","r")
avg=0
sum_1 =0
data_1 =[]
name ={}
for line in input_file:
    
    data= line.split()
    data_1.append(float(data[0]))
    name[data[1]] = data[0]
print(name)
print(data_1)
avg = sum(data_1)/len(data_1)
print("The avarage:",avg)
x=max(data_1)
for key in name:
    if(float(name[key]) == x):
        print("the max:", x, "name: ",key)


#input_file.close()
    #sum_1 = data_1 + sum_1
'''for i in data_1:
    sum_1 = sum_1 + i
    #if data == data[0]:
    avg= sum_1 / len(data_1)
    x=max(data_1)
        #s = avg / len(data[0])
    #avg = sum(data_1) / len(data_1)
    

print(avg,x)
'''


#n=[995.0, 867, 877]
#for i in n:
    #sum_1 = i + sum_1
#print(sum(n))


#sum(data[0])/len(data[0])
#print((877+867+995.0) / 3) 