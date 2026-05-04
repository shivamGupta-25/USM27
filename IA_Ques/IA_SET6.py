'''
Create a 2 two dimension array in 3 rows X 3 columns using numpy library and display array
using nested for loop. Next to Addition the two array using same process without using any
inbuilt numpy library.
'''

import numpy as np

array1 = np.array([
    [21, 22, 23],
    [24, 25, 26],
    [27, 28, 29]
])

array2 = np.array([
    [10, 14, 32],
    [12, 16, 18],
    [14, 13, 15]
])

print("--------- Displaying Array 1 ---------")

for i in range(array1.shape[0]):
    for j in range(array1.shape[1]):
        print(array1[i][j], end=" ")
    print()

print("--------- Displaying Array 2 ---------")

for i in range(array2.shape[0]):
    for j in range(array2.shape[1]):
        print(array2[i][j], end=" ")
    print()


print("------------ Addition of Array 1 and Array 2 --------------")
result = np.zeros((3, 3), dtype=int)

if array1.shape != array2.shape:
    print("For Addition, Both arrays must have the same shape.")
else:
    for i in range(array1.shape[0]):
        for j in range(array1.shape[1]):
            result[i][j] = array1[i][j] + array2[i][j]
            #print(result[i][j], end = " ")
        #print()

print(result)


'''
Write a Program using OOPS to create a class List_Info in which you take any 5 properties
num1, num2, num3, num4 & num5. You create a constructor to initialize the properties of List_Info class.
You create method such as addition(), product(), maximum(), minimum() to List_Info class.
Note: You take any value of properties from num1 to num5. You use Inbuilt function for above
methods.
'''

class List_info:
    def __init__(self, num1, num2, num3, num4, num5):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5

        self.numbers = [num1, num2, num3, num4, num5]
        
    def Addition(self):
        print(f"Addidiotin: {sum(self.numbers)}")

    def Product(self):
        product = 1

        for num in self.numbers:
            product *= num
        
        print(f"Product: {product}")

    def Maximum(self):
        print(f"Maximum: {max(self.numbers)}")

    def Minimum(self):
        print(f"Minimum: {min(self.numbers)}")
    
num1 = int(input("Enter Num 1: "))
num2 = int(input("Enter Num 2: "))
num3 = int(input("Enter Num 3: "))
num4 = int(input("Enter Num 4: "))
num5 = int(input("Enter Num 5: "))

obj1 = List_info(num1, num2, num3, num4, num5)

obj1.Addition()
obj1.Product()
obj1.Maximum()
obj1.Minimum()