new_list=["said,25","majid,19","sailm,32","Ali,21","sultan,28"]
name=[]
'''
age=[]
#for i in lst:
#l=lst.split(",")

#a=age.append(l)
#print(a)
name=[]
def sort1(lst):
    for i in range(len(lst)):
    
        l=lst[i].split(",")
        age.append(int(l[1]))
    print(age)
    
    for i in range(len(lst)):
    
        l=lst[i].split(",")
        name.append(l[0])
    print(name)
'''

def insertsort(new_list):
    for step in range(1,len(new_list)):
        key=new_list[step]
        j=step -1
        while j >= 0 and key.split(",")[1] < new_list[j].split(",")[1]:
            new_list[j+1]=new_list[j]
            j=j-1
        new_list[j+1] =key
        

        




def sort1(new_list):
    for i in range(len(new_list)):
    
        l=new_list[i].split(",")
        name.append(l[0])
    print(name)
    
insertsort(new_list)
print(new_list)
print(sort1(new_list))


