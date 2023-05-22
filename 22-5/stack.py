class stacks:
    
     def __init__(self):
         self.stack=[]
   
     def print_stack(self):
        s="hello"
        for i in s:
            self.stack.append(i)
         
        return self.stack
        
     def reverse(self):
        a=[]
        
        for i in range(len(self.stack)):
            a.append(self.stack.pop())
        return a
s=stacks()
print(s.print_stack())
print(s.reverse())
'''
class stacks:
    
   
    def print_stack():
        
        stack=[]
        stack.append("h")
        stack.append("e")
        stack.append("l")
        stack.append("l")
        stack.append("o")

        a=[]

        print("stacks:" , stack)
        for i in range(len(stack)):
            a.append(stack.pop())
        return a
    
print(stacks.print_stack())'''



'''
stack=[]
stack.append("h")
stack.append("e")
stack.append("l")
stack.append("l")
stack.append("o")

a=[]

print(stack)
for i in range(len(stack)):
    a.append(stack.pop())
print(a)
'''
