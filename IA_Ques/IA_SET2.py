'''
Write a program in python to accept any three numbers and find out which one is greatest
using nested if.
'''

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is Greatest among {num1}, {num2}, and {num3}")
    else:
        print(print(f"{num3} is Greatest among {num1}, {num2}, and {num3}"))
elif num2 > num3:
    print(f"{num2} is Greatest among {num1}, {num2}, and {num3}")
else:
    print(print(f"{num3} is Greatest among {num1}, {num2}, and {num3}"))


'''
Write a program in python using OOPS to create a Base or Parent class Employee have
following properties such as Emp_Id, Emp_name, Designation, and Salary. initialize all of the
properties inside constructor of Base or Parent class. You take two methods Emp_Details() &
Salary_Details()
Again you create another Derived or child class Department with properties Dept_ld,
Dept_name and method name Salary_Incrment(). Initialize all of the properties inside
constructor of Derived or Child class. Calculate Bonus with 20% of Salary.
Note-In which Emp_Id, Emp_name, & Designation will display in Emp_Details() method,
Salary details will display in Salary_Details() method and Salary with Bonus will display in
Salary_Increment() method.
'''

class Employee:
    def __init__(self, emp_id, emp_name, designation, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def Emp_Details(self):
        print("-"*5 + "EMPLOYEE DETAILS" + "-"*5)
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Designation: {self.designation}")

    def Salary_Details(self):
        print("-"*5 + "EMPLOYEE DETAILS" + "-"*5)
        print(f"Salary of Employee {self.emp_name} with Employee ID {self.emp_id} is {self.salary}")

class Department(Employee):
    def __init__(self, emp_id, emp_name, designation, salary, dept_id, dept_name):
        super().__init__(emp_id, emp_name, designation, salary)
        self.dept_id = dept_id
        self.dept_name = dept_name
    
    def Salary_Increment(self):
        bonus = self.salary * 0.2
        total = self.salary + bonus

        print("\n--- Department Details ---")
        print(f"Department ID   : {self.dept_id}")
        print(f"Department Name : {self.dept_name}")

        print("\n--- Salary with Bonus ---")
        print(f"Original Salary : {self.salary}")
        print(f"Bonus (20%)     : {bonus}")
        print(f"Total Salary    : {total}")


employee = Department(101, "Shivam", "Manager",50000, 1,"IT")

employee.Emp_Details()
employee.Salary_Details()
employee.Salary_Increment()