'''
Dic
'''

dict1 = dict()

dict1['E001'] = "Amit"
dict1['E002'] = "Puja"
dict1['E003'] = "Kunal"
dict1['E004'] = "Sandhya"
dict1['E005'] = "Sunil"

# a part change puja to pooja
dict1['E002'] = "Pooja"
print(f"\nOutput After (a) part {dict1}")

print(f"\nName of Employee with ID E003 is {dict1['E003']}")

del dict1['E004']
print(f"\nOutput After (c) part {dict1}\n")

'''
Write a Python program using OOPS take Customer class with following properties Cust_id,
Cust_name, and Purchase of any 4 Products from user. (Book, Marker, Copy & Card_Board).
All of the properties should be instance variables. You take two method Customer_Detail() and
Pay_Details().
In first method you display all the properties including product name.
In second method mention Price of each products, Total_Price and Discount. To evaluate Discount with
following criteria. If Total_Price >= 200 then 20% of Discount on Total_Price otherwise No
Discount.
Note - Price of each product you may take any value.
'''

class Customer:
    def __init__(self, cust_id, cust_name, book, marker, copy, card_board):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.book = book
        self.marker = marker
        self.copy = copy
        self.card_board = card_board

        self.book_price = 120
        self.marker_price = 40
        self.copy_price = 60
        self.cardboard_price = 80

    def customer_details(self):
        print("Customer Details......")
        print("ID:", self.cust_id)
        print("Name:", self.cust_name)

        print("Product Purchased......")
        print(f"Book: {self.book}")
        print(f"Marker: {self.marker}")
        print(f"Copy: {self.copy}")
        print(f"Card Board: {self.card_board}")

    def pay_details(self):
        print("\n----- PAYMENT DETAILS -----")
        
        total_price =  (
            self.book_price * self.book + 
            self.marker_price * self.marker + 
            self.copy_price * self.copy + 
            self.cardboard_price * self.card_board
        )

        print("Total Price: ", total_price)

        if total_price > 200:
            discount = 0.2 * total_price
        else:
            return 0
        
        print(f"Discount : {discount}")
        print(f"Final Amount to Pay : {total_price - discount}")



id = int(input("Enter ID:"))
name = input("Enter Name:")

print("Enter Quntity of Product")
book = int(input("Book:"))
marker = int(input("Marker:"))
copy = int(input("Copy:"))
cardboard = int(input("Card Board:"))

customer = Customer(id, name, book, marker, copy, cardboard)

customer.customer_details()
customer.pay_details()
