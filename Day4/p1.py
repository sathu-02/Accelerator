"""
Problem Statement:

A shopping mall maintains records of vehicles entering its parking area.
Initially, each vehicle is assigned a parking slot number.

For safety and monitoring purposes, the parking management system performs
two inspections every day:

1. Morning Inspection
   - Display the original parking slot allocation of all vehicles.

2. Evening Inspection
   - Reallocate vehicles based on their slot numbers:
     • Slot numbers from 1 to 10  → Basement Parking
     • Slot numbers from 11 to 20 → Ground Floor Parking
     • Slot numbers greater than 20 → First Floor Parking

The parking management system should:

1. Store parking information using a class constructor.
2. Display object information using __repr__().
3. Maintain vehicle-slot mappings using dictionaries.
4. Log report generation using decorators.
5. Perform both inspections automatically using decorators with arguments.
6. Update parking locations during the evening inspection based on slot numbers.

Requirements:
1. Use constructor and __repr__().
2. Use dictionaries.
3. Use if-elif-else conditions.
4. Use decorators.
5. Use decorators with arguments.
6. Preserve function metadata using functools.wraps.

Input Format:
The first line contains an integer N representing the number of vehicles.

The next 2 × N lines contain:
Vehicle Number
Slot Number

Output Format:
Display the parking report for both inspection cycles.

Sample Input:
4
TS09AB1234
12
TS08CD4567
8
TS10EF7890
25
TS07XY4321
18

Sample Output:
Inspection Cycle 1
Generating Parking Report
ParkingReport({'TS09AB1234': 12, 'TS08CD4567': 8, 'TS10EF7890': 25, 'TS07XY4321': 18})

Inspection Cycle 2
Generating Parking Report
ParkingReport({'TS09AB1234': 'Ground Floor Parking', 'TS08CD4567': 'Basement Parking', 'TS10EF7890': 'First Floor Parking', 'TS07XY4321': 'Ground Floor Parking'})

"""
from functools import wraps

class ParkingReport:
    def __init__(self,report):
        self.report=report
    
    def __repr__(self):
        return f"ParkingReport({self.report})"
    
    def retry(retries=2):
        def decorator(alloc):
            @wraps(alloc)
            def wrapper(self):
                for i in range(retries):
                    try:
                        print(f"Inspection Cycle {i+1}")
                        print("Generating Parking Report")
                        print(alloc(self,i+1))
                    except Exception as e:
                        print(e)
            return wrapper
        return decorator
        
    @retry(2)
    def alloc(self,a):
        if a==2:
    
            vehicles=list(self.report.keys())
            for i in vehicles:
                if self.report[i]>0 and self.report[i]<11:
                    self.report[i]="Basement Parking"
                elif self.report[i]>10 and self.report[i]<21:
                    self.report[i]="Ground Floor Parking"
                elif self.report[i]>20:
                    self.report[i]="First Floor Parking"
            #self.report=report
            return repr(self)
        elif a==1:
            return repr(self)
            
n=int(input())
d={}
for i in range(n):
    v=input()
    s=int(input())
    d[v]=s
pr=ParkingReport(d)
pr.alloc()
            
        
                    
                    
    












































