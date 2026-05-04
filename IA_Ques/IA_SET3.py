'''
Armstrong number
'''

num = int(input("Enter the Number: "))

n = int(len(str(num)))

temp = num
sum = 0

while temp != 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")


'''
Write a program in python using OOPS to create a class Flight. Properties of the Flight class are
Flight_id, Cust_name, Journey_from, Journey_to, Distance & Fare. You initialize all of the
properties inside constructor. 
You define two methods Flight_info() and Fare_info(). 
In first method you display all of the properties. 
In Second method calculate total Fare according to following condition. 
If Distance is greater and equal to 2000 then New_Fare will Discount 30% of its Fare otherwise New_Fare will Discount 15% of its Fare.

Note - All the properties are taken by user using keyboard function.
'''

class Flight:
    def __init__(self, flight_id, cust_name, journey_from, journey_to, distance, fare):
        self.flight_id = flight_id
        self.cust_name = cust_name
        self.journey_from = journey_from
        self.journey_to = journey_to
        self.distance = distance
        self.fare = fare

    def flight_info(self):
        print("---------- Flight Info------------")
        print(f"Flight ID: {self.flight_id}")
        print(f"Customer Name: {self.cust_name}")
        print(f"Journey From: {self.journey_from}")
        print(f"Journey To: {self.journey_to}")
        print(f"Distance: {self.distance}")
        print(f"Fare: {self.fare}")

    def fair_info(self):
        print("--------- FARE DETAILS-----------")

        if self.distance >= 2000:
            discount = 0.3 * self.fare
        else:
            discount = 0.15 * self.fare

        print("Original fair: ", self.fare)
        print("Discount: ", discount)
        print("Final Fare: ", self.fare - discount)

flight_id = input("Enter Flight ID:")
cust_name = input("Enter Customer Name:")
journey_from = input("Enter Journey From:")
journey_to = input("Enter Journey To:")
distance = float(input("Enter Distance:"))
fare = float(input("Enter Fare:"))

# Create object
f1 = Flight(flight_id, cust_name, journey_from, journey_to, distance, fare)

# Call methods
f1.flight_info()
f1.fair_info()