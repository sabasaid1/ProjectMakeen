class person:
    no_person=0
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        person.no_person +=1
    def descrip(self):
        return f"person {self.name} and age {self.__age}"
    def set_age(self,new_age):
        self.__age=new_age
    
p1 = person("said",22)
p2 = person("Ali",23)

print(p1.descrip())
print(p1.no_person)
p2.set_age(40)
p2.age=42
print(p2.descrip())