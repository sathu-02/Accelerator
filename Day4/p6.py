"""

Problem Statement:

An insurance company provides policies for:

1. Car
2. Bike

Both inherit from Vehicle.

Override premium calculation methods.

Car Premium = Vehicle Cost × 5%

Bike Premium = Vehicle Cost × 3%

If vehicle cost is negative, display:

Invalid Vehicle Cost

Input Format:
Vehicle Type (Car / Bike)
Vehicle Cost

Output Format:
Display premium amount.

Sample Input:
Car
500000

Sample Output:
Premium = 25000.0

case=1
input=Car
500000

output=
Premium = 25000.0

case=2
input=Bike
100000

output=
Premium = 3000.0

case=3
input=Car
250000

output=
Premium = 12500.0

case=4
input=Bike
75000

output=
Premium = 2250.0

case=5
input=Car
-50000

output=
Invalid Vehicle Cost
"""
class InvalidCost(Exception):
    pass

class Vehicle:
    def __init__(self,v_type, v_cost):
        self.v_type=v_type
        self.v_cost=v_cost
    def cal_prem(self):
        return 1
class Car(Vehicle):
    def cal_prem(self):
        return (self.v_cost*0.05)
class Bike(Vehicle):
    def cal_prem(self):
        return (self.v_cost*0.03)

v_type=input().strip()
v_cost=int(input())

try:
    if v_cost<0:
        raise InvalidCost("Invalid Vehicle Cost")
    if v_type.lower()=="car":
        v=Car(v_type,v_cost)
        print(f"Premium = {v.cal_prem()}")
    elif v_type.lower()=="bike":
        v=Bike(v_type,v_cost)
        print(f"Premium = {v.cal_prem()}")
except Exception as e:
    print(e)
