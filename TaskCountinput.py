
sides=int(input("enter side:"))

def main():
    x =countInputs(sides)
    printCounters(x)

def countInputs(sides):
    
    counters=[0]*(sides+1)
    
    for i in counters:
        v=int(input("enter num:"))
        
        if v <= 6 :
            counters[v] = counters[v] + 1
        
    return counters
    
    
def printCounters(counters):
    
    for i in range(1,len(counters)):
        print(i,":",counters[i])
        
        
main()
