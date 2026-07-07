"""
Problem Statement:
Write a function that accepts student information using **kwargs
and displays all key-value pairs.

Input Format:
Student name
Student age
Student branch

Output Format:
Display all student details.

Sample Input:
Ravi
20
CSE

Sample Output:
name : Ravi
age : 20
branch : CSE
"""
def display(**kwargs):
    print(kwargs)
    
s_name=input()
s_age=int(input())
s_branch=input()

display(name=s_name, age=s_age, branch=s_branch)
