"""
A software company processes the monthly payroll of its employees.

Each employee record contains:

Employee ID
Employee Name
Department
Basic Salary
Bonus

The bonus may or may not be available for every employee.

The payroll system should calculate the Net Salary using the following formula:

Net Salary = Basic Salary + Bonus

If the bonus is not available, it should be treated as 0.

Store all employee records using a dictionary where: Employee ID → (Employee Name, Department, Basic Salary, Bonus)

After processing all employees, display the employee payroll sorted in descending order of Net Salary.

The payroll calculation function should use Python Type Hints.

The bonus parameter should use Optional.

The salary values should use Union[int, float].

Requirements:
---------------
Store employee records using a dictionary.
Create a payroll calculation function using Type Hints.
Use Optional for Bonus.
Use Union[int, float] for salary values.
Sort employees using a lambda expression.
Display Net Salary for every employee.

Input Format
-------------
The first line contains the number of employees N.
The next N sets contain:
Employee ID
Employee Name
Department
Basic Salary
Bonus

If bonus is not available, the input will be:None

Output Format:
---------------
Employee Payroll:

E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000


sample input:
3
E101
Ravi
Development
60000
5000
E102
Priya
HR
50000
None
E103
Rahul
Testing
55000
1000

Sample Output:
Employee Payroll:
E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000

Test Cases
-----------
case=1
input=3
E101
Ravi
Development
60000
5000
E102
Priya
HR
50000
None
E103
Rahul
Testing
55000
1000
output=
Employee Payroll:
E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000

case=2
input=2
E201
Anu
Testing
40000
None
E202
Kiran
Development
45000
5000
output=
Employee Payroll:
E202 -> Kiran -> Development -> 50000
E201 -> Anu -> Testing -> 40000

case=3
input=1
E301
Ajay
HR
35000
2500
output=
Employee Payroll:
E301 -> Ajay -> HR -> 37500


case=4
input=1
E401
Ramesh
Testing
-5000
1000
output=
Invalid Basic Salary


case=5
input=1
E501
Pooja
Development
45000
-500
output=
Invalid Bonus

case=6
input=0
output=
Invalid Number of Employees
"""
from typing import Optional,Union

class InvalidEmployees(Exception):
    pass
class InvalidSal(Exception):
    pass
class InvalidBonus(Exception):
    pass

def cal_sal(lst) -> None:
    for i in lst:
        print(f"{i[0]} -> {i[1][0]} -> {i[1][1]} -> {int(i[1][2]+i[1][3])}")
    
    

try:
    n=int(input().strip())
    if n<=0:
        raise InvalidEmployees("Invalid Number of Employees")
    
    d={}
    for i in range(n):
        eid: str=input().strip()
        name: str=input().strip()
        dept:str=input().strip()
        sal: int|float=float(input().strip())
        b=input().strip()
        if b=="None":
            bonus:Optional[Union[int,float]]=None
        else:
            bonus=float(b)
        if bonus==None:
            bonus=0
        d[eid]=(name,dept,sal,bonus)
    for i in d.items():
        if i[1][2]<=0:
            raise InvalidSal("Invalid Basic Salary")
        if i[1][3]<0:
            raise InvalidBonus("Invalid Bonus")
            
    print("Employee Payroll:")
    lst=list(d.items())
    lst.sort(key=lambda x:x[1][2]+x[1][3],reverse=True)
    cal_sal(lst)
except Exception as e:
    print(e)

    
    


    
