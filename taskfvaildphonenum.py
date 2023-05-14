string = input("enter phone num (XXX)XXX-XXXX:")
vaild = len(string)==13
postion = 0
while vaild and postion <len(string):
    if postion == 0:
        vaild = string[postion] == "("
    elif postion == 4:
        vaild = string[postion] == ")"
    elif postion == 8:
        vaild = string[postion] == "-"
    else:
        vaild = string[postion].isdigit()
    postion = postion+1
    
    
if vaild :
    print("The sting contain a vaild number")
else:
    print("The sting contain is not vaild")
    
