import numpy as np

x1 = np.array([-10,-10,0,8,10])
x2 = np.array([-10,0,8,10,-10])
y1 = np.array([20,20,3,17,-16])
y2 = np.array([-18,3,17,-16,-18])

s1 = ((x1[0] - x2[0])**2 + (y1[0] - y2[0])**2)**0.5
s2 = ((x1[1] - x2[1])**2 + (y1[1] - y2[1])**2)**0.5
s3 = ((x1[2] - x2[2])**2 + (y1[2] - y2[2])**2)**0.5
s4 = ((x1[3] - x2[3])**2 + (y1[3] - y2[3])**2)**0.5
s5 = ((x1[4] - x2[4])**2 + (y1[4] - y2[4])**2)**0.5

slops1 = (y2[0]-y1[0])/(x2[0]-x1[0])
slops2 = (y2[1]-y1[1])/(x2[1]-x1[1])
slops3 = (y2[2]-y1[2])/(x2[2]-x1[2])
slops4 = (y2[3]-y1[3])/(x2[3]-x1[3])
slops5 = (y2[4]-y1[4])/(x2[4]-x1[4])

print("s1 length: ", s1," slop: ",slops1)
print("s2 length: ", s2," slop: ",slops2)
print("s3 length: ", s3," slop: ",slops3)
print("s4 length: ", s4," slop: ",slops4)
print("s5 length: ", s5," slop: ",slops5)

y=np.concatenate((y1,y2))


print("max y:",max(y))
print("min y:",min(y))




