"""
Problem Statement:

A company stores employee information in a database.

Whenever an employee record is accessed, the application
should automatically establish a database connection.

After processing the employee records, the database
connection should be closed automatically, irrespective
of whether the operation completes successfully or an
exception occurs.

If an invalid employee salary (less than or equal to zero)
is entered, raise an exception and display:

Invalid Employee Salary

The database connection must still be closed automatically.

Requirements:
1. Create a Context Manager using __enter__() and __exit__().
2. Use the with statement.
3. Use Exception Handling.
4. Raise an exception for invalid salary.
5. Store employee details using a dictionary.
6. Ensure the database connection closes even when an
   exception occurs.

Input Format:
First line contains the number of employees.

Next N sets contain:

Employee ID
Employee Name
Salary

Output Format:

Connecting to Database...
Employee Details:
EMP101 -> Ravi -> 50000
EMP102 -> Priya -> 60000
Database Connection Closed

If salary is invalid, display:

Invalid Employee Salary

Sample Input:
2
EMP101
Ravi
50000
EMP102
Priya
60000

Sample Output:
Connecting to Database...
Employee Details:
EMP101 -> Ravi -> 50000
EMP102 -> Priya -> 60000
Database Connection Closed


case=1
input=
2
EMP101
Ravi
50000
EMP102
Priya
60000

output=
Connecting to Database...
Employee Details:
EMP101 -> Ravi -> 50000
EMP102 -> Priya -> 60000
Database Connection Closed


case=2
input=
1
EMP201
Kiran
75000

output=
Connecting to Database...
Employee Details:
EMP201 -> Kiran -> 75000
Database Connection Closed

case=3
input=
2
EMP101
Ravi
-5000
EMP102
Priya
60000

output=
Connecting to Database...
Database Connection Closed
Invalid Employee Salary

case=4
input=
2
EMP101
Ravi
0
EMP102
Priya
50000

output=
Connecting to Database...
Database Connection Closed
Invalid Employee Salary

case=5
input=
0

output=
Invalid Number of Employees

case=6
input=
-2

output=
Invalid Number of Employees
"""
class InvalidEmployees(Exception):
    pass
class InvalidSalary(Exception):
    pass

class ConnectionSession:
    def __enter__(self):
        print("Connecting to Database...")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print("Database Connection Closed")
        return False

def empDetails(d):
    
    for i in d.values():
        if i[1]<=0:
            raise InvalidSalary("Invalid Employee Salary")
    print("Employee Details:")
    for i in d.items():
        print(f"{i[0]} -> {i[1][0]} -> {i[1][1]}")
   

try:
    n=int(input().strip())
    if n<=0:
        raise InvalidEmployees("Invalid Number of Employees")
    d={}
    for i in range(n):
        eid=input().strip()
        name=input().strip()
        sal=int(input().strip())
        d[eid]=[name,sal]
    with ConnectionSession():
        empDetails(d)
except Exception as e:
    print(e)
