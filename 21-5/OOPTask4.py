class resturant:
    def __init__(self):
        self.menu_item={}
        self.book_table=[]
        self.customer_orders =[]
    def add_menu_item(self,item,price):
        self.menu_item[item] = price
    def book_tables(self,table_number):
        self.book_table.append(table_number)
    def customer_order(self,table_number,order):
        order_details = {'table anumber':table_number,'order':order}
        self.customer_orders.append(order_details)
    def print_menu(self):
        for item,price in self.menu_item.items():
            print(f"{item} , {price}")
    def print_table_reservation(self):
        for table in self.book_table:
            print(f"table {table}")
    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))
        
restaurant = resturant()

restaurant.add_menu_item("pizaa",2.5)
restaurant.book_tables(1)
restaurant.customer_orders(1, "pizaa")

restaurant.print_menu()
restaurant.print_table_reservation()
restaurant.print_customer_orders()


