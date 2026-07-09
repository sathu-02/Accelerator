"""


Problem Statement:

A railway department maintains passenger records.

Create a base class Passenger.

Create two derived classes:

1. SleeperClass
   - Fare = Distance × ₹2

2. ACClass
   - Fare = Distance × ₹4

Override the fare calculation method.

If distance is negative, display:

Invalid Distance

Input Format:
Class Type (Sleeper / AC)
Passenger Name
Distance

Output Format:
Display fare amount.

Sample Input:
AC
Priya
100

Sample Output:
Fare = 400
"""
class InvalidDistanceError(Exception):
    pass

class Passenger:
    def __init__(self,cl,name,dist):
        self.cl=cl
        self.name=name
        self.dist=dist
    def calculate_fare(self):
        return self.dist

class SleeperClass(Passenger):
    def __init__(self,cl,name,dist):
        super().__init__(cl,name,dist)
    def calculate_fare(self):
        return self.dist*2

class ACClass(Passenger):
    def __init__(self,cl,name,dist):
        super().__init__(cl,name,dist)
    def calculate_fare(self):
        return self.dist*4
        
try:
    cl=input()
    name=input()
    dist=int(input())
    if dist<0:
        raise InvalidDistanceError("Invalid Distance")
    else:
        if cl.lower()=="ac":
            p=ACClass(cl,name,dist)
            res=p.calculate_fare()
            print(f"Fare = {res}")
        elif cl.lower()=="sleeper":
            p=SleeperClass(cl,name,dist)
            res=p.calculate_fare()
            print(f"Fare = {res}")
except Exception as e:
    print(e)
            
    
