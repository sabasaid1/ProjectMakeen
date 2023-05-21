class Employee:
    
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.__emp_department = emp_department
        
        
    def assign_department(self,new_department):
        self.__emp_department=new_department
    def print_employee_details(self):
        return f"name {self.emp_name} and id {self.emp_id} and salary {self.emp_salary} and department {self.__emp_department}"
    
    def calculate_emp_salay(self,hw):
        if hw > 50:
            overtime = hw -50
            amount=(overtime * (self.emp_salary/50))
            return amount
        else:
            return self.emp_salary
            
        
    
e1 = Employee("E7867" , "ADAMS" , 50000,"Accounting")
e2 = Employee("E7867" , "Join" ,  45000,"SALES")
e3 = Employee("E7867" , "ADAMS" , 50000,"Accounting")
e4 = Employee("E7867" , "ADAMS" , 55000,"Accounting")

print(e1.print_employee_details())
e2.assign_department("IT")
print(e2.print_employee_details())
print(e2.calculate_emp_salay(60))






        
        
        
    