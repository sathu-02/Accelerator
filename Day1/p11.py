"""
Problem Statement:
Override the __str__ method to display object information.

Input Format:
Student name

Output Format:
Display formatted student information.

Sample Input:
Ravi

Sample Output:
Student Name: Ravi
"""

class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Name: {self.name}"
class Student(Person):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f"Student Name: {self.name}"

s_name=input()
s=Student(s_name)
print(s)

        

