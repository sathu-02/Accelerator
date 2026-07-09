"""

Problem Statement:

A library supports two membership categories:

1. Student Member
   - Maximum books allowed = 3

2. Faculty Member
   - Maximum books allowed = 5

Override the borrow limit method.

If requested books exceed the limit, display:

Borrow Limit Exceeded

Input Format:
Member Type (Student / Faculty)
Member Name
Number of Books

Output Format:
Display borrowing status.

Sample Input:
Student
Ravi
2

Sample Output:
Books Issued Successfully

case=1
input= Student
Ravi
2

output=
Books Issued Successfully

case=2
input= Student
Priya
3

output=
Books Issued Successfully

case=3
input=Student
John
4

output=
Borrow Limit Exceeded

case=4
input=Faculty
Kiran
5

output=
Books Issued Successfully

case=5
input=Faculty
Swetha
6

output=
Borrow Limit Exceeded

case=6
input=Faculty
David
0

output=
Books Issued Successfully


case=7
input=Student
Anu
1

output=
Books Issued Successfully
"""
class BorrowLimit(Exception):
    pass
class InvalidRole(Exception):
    pass
class Library:
    def __init__(self,role,name):
        self.role=role
        self.name=name
    def borrow_limit(self):
        return 1
class StudentRole(Library):

    def borrow_limit(self):
        return 3
class FacultyRole(Library):

    def borrow_limit(self):
        return 5
        
        
try:
    role=input().strip()
    name=input().strip()
    req=int(input())
    
    if role.lower() not in ["student", "faculty"]:
        raise InvalidRole("Invalid Membership")
    
    if role.lower()=="student":
        l=StudentRole(role,name)
        if(l.borrow_limit()>=req):
            print("Books Issued Successfully")
        else:
            raise BorrowLimit("Borrow Limit Exceeded")
            
    elif role.lower()=="faculty":
        l=FacultyRole(role,name)
        if(l.borrow_limit()>=req):
            print("Books Issued Successfully")
        else:
            raise BorrowLimit("Borrow Limit Exceeded")
except Exception as e:
    print(e)
        
            
        
