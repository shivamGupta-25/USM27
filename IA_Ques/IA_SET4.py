'''
Write a program in python to accept a String and reverse the String in Another variable. Find
after reversing both Strings are Palindrome or not. Finally, you add the sum of the characters
in the String.
Note-String in the form of word or sentence should be taken by user.
'''

value = input("Enter the Input: ")
pal = ''

for i in range(len(value), 0, -1):
    pal += value[i-1]

if pal == value:
    print("Given string is Palindrome")
else:
    print("Given string is not Palindrome")

# Sum of characters (ASCII values)
char_sum = 0
for ch in value:
    char_sum += ord(ch)

print("Sum of ASCII values of characters:", char_sum)


'''
Create a Base class name Shape with Derived or subclasses like Triangle and Square to
calculate area and perimeter using standard formulas.
In shape class properties name topic and dimension and a function name show_Shape().
in triangle properties is base and height and function name area_Triangle() and peri_Triangle()
in square properties is side and function name area_Sqr() and peri_Sqr()
Note: topic display geometry and dimension is 1D, 2D, 3D. Consider Triangle is Right Angle Triangle.
'''
import math

class Shape:
    def __init__(self, topic, dimension):
        self.topic = topic
        self.dimension = dimension

    def show_shape(self):
        print(f"Topic: {self.topic}")
        print(f"Dimension: {self.dimension}")

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Geometry", "2D")
        self.base = base
        self.height = height
    
    def area_triangle(self):
        return 0.5 * self.base * self.height
    
    def peri_triangle(self):
        # Hypotenuse using Pythagoras theorem
        hypotenuse = math.sqrt(self.base**2 + self.height**2)
        return self.base + self.height + hypotenuse
    
class Square(Shape):
    def __init__(self, side):
        super().__init__("Geometry", "2D")
        self.side = side

    def area_sqr(self):
        return self.side**2
    
    def peri_sqr(self):
        return 4*self.side
    

print("-"*5 + "TRIANGLE" + "-"*5)
triangle = Triangle(3, 4)
triangle.show_shape()

print(f"Area of Triangle: {triangle.area_triangle()}")
print(f"Perimeter of Triangle: {triangle.peri_triangle()}")

print("-"*5 + "SQUARE" + "-"*5)
square = Square(3)
square.show_shape()

print(f"Area of square: {square.area_sqr()}")
print(f"Perimeter of square: {square.peri_sqr()}")

