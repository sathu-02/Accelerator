"""
Problem Statement:
A company wants to store employee information efficiently.
Create an Employee class using __slots__ to restrict attributes
to employee ID, name, and salary.

Input Format:
Employee ID
Employee Name
Employee Salary

Output Format:
Display employee details.

Sample Input:
101
Ravi
50000

Sample Output:
Employee ID: 101
Employee Name: Ravi
Employee Salary: 50000
"""
class Employee:
    __slots__=["empId", "name", "sal"]
    
    def __init__(self,empId,name,sal):
        self.name=name
        self.empId=empId
        self.sal=sal
    def __str__(self):
        return f"Employee ID: {self.empId}\nEmployee Name: {self.name}\nEmployee Salary: {self.sal}"
        
e=Employee(int(input()), input(), int(input()))
print(e)

