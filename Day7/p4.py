"""

Problem Statement:

An e-commerce company wants to recommend the best products
to its customers based on customer ratings.

Each product record contains:

Product ID
Product Name
Product Price
Customer Rating

The product price may be either an integer or a
floating-point value.

The recommendation system evaluates products using two
different methods.

Method 1:
Find the highest rated product using a traditional
for loop.

Method 2:
Find the highest rated product using Python's built-in
max() function.

Instead of measuring execution time, compare the
performance by counting the number of operations
performed by each method.

Store all product records using a dictionary where

Product ID → (Product Name, Product Price, Rating)

The functions should use Python Type Hints.

The product price should use Union[int, float].

After processing all products:

• Display products sorted in descending order of rating.

• Display the highest rated product using both methods.

• Display the number of operations performed by each method.

• Display the better performing method.

Requirements:
-------------
1. Store product records using a dictionary.
2. Use Python Type Hints.
3. Use Union[int, float].
4. Implement Method 1 using a for loop.
5. Implement Method 2 using max().
6. Sort products using a lambda expression.
7. Count the number of operations.
8. Display the better performing method.

Input Format:
-------------
First line contains the number of products N.

Next N sets contain:

Product ID
Product Name
Product Price
Customer Rating

Output Format:
--------------
Recommended Products:

P101 -> Laptop -> 65000 -> 4.9
P103 -> Camera -> 35000 -> 4.8
P102 -> Mobile -> 25000 -> 4.5

Method 1 Highest Rating : 4.9

Method 2 Highest Rating : 4.9

Method 1 Operations : 3

Method 2 Operations : 1

Better Performing Method : Method 2

Sample Input:
-------------
3
P101
Laptop
65000
4.9
P102
Mobile
25000
4.5
P103
Camera
35000
4.8

Sample Output:
--------------
Recommended Products:
P101 -> Laptop -> 65000 -> 4.9
P103 -> Camera -> 35000 -> 4.8
P102 -> Mobile -> 25000 -> 4.5

Method 1 Highest Rating : 4.9

Method 2 Highest Rating : 4.9

Method 1 Operations : 3

Method 2 Operations : 1

Better Performing Method : Method 2

Test Cases:
-----------

case=1
input=
3
P101
Laptop
65000
4.9
P102
Mobile
25000
4.5
P103
Camera
35000
4.8

output=
Recommended Products:
P101 -> Laptop -> 65000 -> 4.9
P103 -> Camera -> 35000 -> 4.8
P102 -> Mobile -> 25000 -> 4.5

Method 1 Highest Rating : 4.9

Method 2 Highest Rating : 4.9

Method 1 Operations : 3

Method 2 Operations : 1

Better Performing Method : Method 2


case=2
input=
2
P201
Keyboard
1200
4.3
P202
Mouse
800
4.7

output=
Recommended Products:
P202 -> Mouse -> 800 -> 4.7
P201 -> Keyboard -> 1200 -> 4.3

Method 1 Highest Rating : 4.7

Method 2 Highest Rating : 4.7

Method 1 Operations : 2

Method 2 Operations : 1

Better Performing Method : Method 2


case=3
input=
1
P301
Monitor
15000
4.8

output=
Recommended Products:
P301 -> Monitor -> 15000 -> 4.8

Method 1 Highest Rating : 4.8

Method 2 Highest Rating : 4.8

Method 1 Operations : 1

Method 2 Operations : 1

Better Performing Method : Both Methods


case=4
input=
0

output=
Invalid Number of Products


case=5
input=
2
P401
Printer
12000
4.5
P402
Scanner
9000
5.5

output=
Invalid Rating
"""
from typing import List, Union, Tuple, Dict

class InvalidProducts(Exception):
    pass
class InvalidRating(Exception):
    pass
def method1(d:Dict[str,Tuple[str,Union[int,float],float]]) -> Tuple[float,int,str]:
    maxi=0.0
    count=0
    pro=""
    for pid,details in d.items():
        count+=1
        if details[2]>maxi:
            #count+=1
            pro=pid
            maxi=details[2]
    return (maxi,count,pro)

def method2(d:Dict[str,Tuple[str,Union[int,float],float]]) -> Tuple[float,int,str]:
   high=max(d.items(),key=lambda x:x[1][2])
   count=1
   return (high[1][2],count,high[0])
        
try:
    n=int(input().strip())
    if n<=0:
        raise InvalidProducts("Invalid Number of Products")
    d:Dict[str,Tuple[str,Union[int,float],float]]={}
    for i in range(n):
        pid:str=input().strip()
        name:str=input().strip()
        price: Union[int,float]=float(input().strip())
        rating:float=float(input().strip())
        d[pid]=(name,price,rating)
    for i in d.items():
        if i[1][-1]>5 or i[1][-1]<0:
            raise InvalidRating("Invalid Rating")
    
    res1=method1(d)
    res2=method2(d)
    
    sorted_pro=sorted(d.items(),key=lambda x:x[1][2],reverse=True)
    print("Recommended Products:")
    for pid,details in sorted_pro:
        print(f"{pid} -> {details[0]} -> {int(details[1])} -> {details[2]}")
    print()
    print(f"Method 1 Highest Rating : {res1[0]}")
    print()
    print(f"Method 2 Highest Rating : {res2[0]}")
    print()
    print(f"Method 1 Operations : {res1[1]}")
    print()
    print(f"Method 2 Operations : {res2[1]}")

    if res1[1]<res2[1]:
        better="Method 1"

    elif res1[1]>res2[1]:
        better="Method 2"

    else:
        better="Both Methods"
    print()
    print(f"Better Performing Method : {better}")


except Exception as e:
    print(e)
        
