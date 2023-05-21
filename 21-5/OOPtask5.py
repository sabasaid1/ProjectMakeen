class BankAccount:
    def __init__(self,account_nmber,balance,date_of_opening,customer_name):
        self.account_nmber = account_nmber
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def descrip(self):
        return f"person {self.account_nmber} and {self.balance} and {self.date_of_opening} and {self.customer_name} "
    def deposit(self,amount):
        
        self.balance += amount
        print(f" amount deposit {amount}")
        
    def withdraw(self ,amount):
        if amount > self.balance:
            print("can not")
        else:
            self.balance -= amount
            print(f"amount withdraw:{amount}")
            
    def check_balance(self):
        print(f" balance {self.balance}")
        
        
        
        
        
    #def check_balance():
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_nmber)
        print("Date of opening:", self.date_of_opening)
        print(f"Balance: ${self.balance}\n")
        
b1 = BankAccount(12341,2000,"2022-06-10","said")
print(b1.descrip())

b1.deposit(20)
#b1.check_balance()
b1.print_customer_details()
b1.withdraw(300)
#b1.check_balance()
b1.print_customer_details()

#print(b1.deposit(amount))

        