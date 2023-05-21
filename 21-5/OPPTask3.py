from datetime import date

class person:
    
    def __init__(self,name,age,addres,hours):
        self.name = name
        self.age = age
        self.addres = addres
        self.hours = hours
        
    def descrip(self):
        return f"person {self.name} and age {self.age}"
    #def set_age(self,new_age):
    def class_type(self):
        return "This is Parent calss"

        self.__age=new_age
class student(person):
    
    def __init__(self,name,age,addres,hours,grade):
        super().__init__(name,age,addres,hours)
        self.grade = grade
        
    def class_type(self):
        return "This is student calss"
    
    @classmethod
    def new_student(cls,name,brith_year,addres,hours,grade):
        return cls(name,date.today().year - brith_year,addres,hours,grade)
    


s1 = student("Salim" , 23,"Muscat",180,[3.1,2.5,2])
p1 = person("Salim" , 23,"Muscat",180)
print(s1.class_type())
print(p1.class_type())

s2 = student.new_student("Salim" , 1998,"Muscat",180,[3.1,2.5,2])

print(date.today())
print("age",s2.age)
    
    
#p1 = person("said",22)
#p2 = person("Ali",23)

#print(p1.descrip())
#print(p1.no_person)
#p2.set_age(40)
#p2.age=42
#print(p2.descrip())