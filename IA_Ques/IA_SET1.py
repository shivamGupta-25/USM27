'''
Write a program in Python to create two empty Tuple, Then ask from user to how many
product to insert into the tuple and then finally display each product name and its price in
Tuple. Finally calculate Total_Price of these products
Note - there is no need to take any inbuilt function to solve above program.
'''

product = tuple()
price = tuple()

n = int(input("Enter the number of product required: "))

for i in range (n):
    product_name = input(f"Enter Product {i+1}: ")
    product_price = int(input(f"Enter Price of Product {i+1}: "))

    product += (product_name,)
    price += (product_price,)

print("\n----- PRODUCT DETAILS -----")
print("(Product Price)")
print(list(zip(product, price)))

print("\n----- TOTAL PRICE -----")
print(f"Total Price: {sum(price)}")

'''
Write a program in python using OOPS to create a class Product have following properties such
as Product_Id, Product_name, Brand_name, Price and Discount. Declare Product Id.
Product_name, Brand_name are class variable while Price and Discount are instance variable

You take three functions Price(), Discount() and Pay_amount().
Note- In which price amount display in Price() methods, Discount amount display in Discount()
method and amount paid by customer to be display in Pay_amount() methods. Discount value
take in percent.
'''

class Product:
    # Class variables
    product_id = None
    product_name = None
    brand_name = None

    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    def calculate_discount_amount(self):
        return (self.discount / 100) * self.price

    def Price(self):
        print("-------- PRICE DETAILS ------------")
        print(f"Product ID: {Product.product_id}")
        print(f"Product Name: {Product.product_name}")
        print(f"Brand Name: {Product.brand_name}")
        print(f"Price: {self.price}")

    def Discount(self):
        print("----------- DISCOUNT DETAILS ------------")
        print(f"Discount (%): {self.discount}%")
        print("Discount Amount:", self.calculate_discount_amount())

    def Pay_amount(self):
        print("----------- PAYMENT DETAILS -------------")
        final = self.price - self.calculate_discount_amount()
        print(f"Final Amount to Pay : {final}")


# Input
Product.product_id = input("Enter Product ID: ")
Product.product_name = input("Enter Product Name: ")
Product.brand_name = input("Enter Brand Name: ")

price = float(input("Enter Price: "))
discount = float(input("Enter Discount (%): "))

p1 = Product(price, discount)

p1.Price()
p1.Discount()
p1.Pay_amount()