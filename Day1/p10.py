"""
Problem Statement:
Create a Person class and inherit it in Employee class.

Input Format:
Employee name

Output Format:
Display employee name.

Sample Input:
Ravi

Sample Output:
Employee: Ravi
"""

class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name):
        super().__init__(name)
e_name=input()
e=Employee(e_name)
print(f"Employee: {e.name}")
