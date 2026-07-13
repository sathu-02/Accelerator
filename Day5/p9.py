"""
Problem Title: Smart Library Book Lending System

Problem Statement:

A digital library maintains records of books issued to members.

Every day, the library management system performs two report
generation cycles:

1. Morning Report
2. Evening Report

During each report generation, the system should display all
currently issued books.

Instead of displaying all issued books together, the system
should generate one issued book record at a time using a
generator function.

After generating the report, the librarian wants to verify
each generated record one by one using an iterator.

Before generating every report, the system should display:

Generating Library Report...

using a decorator.

The report generation should automatically execute twice
(Morning and Evening) using a decorator with arguments.

Requirements:
1. Use a dictionary to store Book ID and Student Name.
2. Use a generator function with yield.
3. Use an iterator using iter() and next().
4. Use a decorator.
5. Use a decorator with arguments.
6. Preserve function metadata using functools.wraps.

Input Format:
First line contains the number of issued books.

Next N sets of input contain:

Book ID
Student Name

Output Format:

Morning Report
Generating Library Report...
Book101 -> Ravi
Book102 -> Priya

Verified Records:
Book101 -> Ravi
Book102 -> Priya

Evening Report
Generating Library Report...
Book101 -> Ravi
Book102 -> Priya

Verified Records:
Book101 -> Ravi
Book102 -> Priya

Sample Input:
2
Book101
Ravi
Book102
Priya

Sample Output:
Morning Report
Generating Library Report...
Book101 -> Ravi
Book102 -> Priya

Verified Records:
Book101 -> Ravi
Book102 -> Priya

Evening Report
Generating Library Report...
Book101 -> Ravi
Book102 -> Priya

Verified Records:
Book101 -> Ravi
Book102 -> Priya

case=1
input=2
Book101
Ravi
Book102
Priya

output=
Morning Report
Generating Library Report...
Book101 -> Ravi
Book102 -> Priya

Verified Records:
Book101 -> Ravi
Book102 -> Priya

Evening Report
Generating Library Report...
Book101 -> Ravi
Book102 -> Priya

Verified Records:
Book101 -> Ravi
Book102 -> Priya

case=2
input=1
Book201
Kiran

output=
Morning Report
Generating Library Report...
Book201 -> Kiran

Verified Records:
Book201 -> Kiran

Evening Report
Generating Library Report...
Book201 -> Kiran

Verified Records:
Book201 -> Kiran


case=3
input=3
B101
Ravi
B102
Anu
B103
Rahul

output=
Morning Report
Generating Library Report...
B101 -> Ravi
B102 -> Anu
B103 -> Rahul

Verified Records:
B101 -> Ravi
B102 -> Anu
B103 -> Rahul

Evening Report
Generating Library Report...
B101 -> Ravi
B102 -> Anu
B103 -> Rahul

Verified Records:
B101 -> Ravi
B102 -> Anu
B103 -> Rahul

case=4
input=0

output=
Invalid Number of Books

case=5
input=-2

output=
Invalid Number of Books

case=6
input=2
Python101
Swetha
Java102
Mahesh

output=
Morning Report
Generating Library Report...
Python101 -> Swetha
Java102 -> Mahesh

Verified Records:
Python101 -> Swetha
Java102 -> Mahesh

Evening Report
Generating Library Report...
Python101 -> Swetha
Java102 -> Mahesh

Verified Records:
Python101 -> Swetha
Java102 -> Mahesh
"""

from functools import wraps

class InvalidBooks(Exception):
    pass

def retry(retries=2):
    def decorator(gen_and_verify):
        @wraps(gen_and_verify)
        def wrapper(*args):
            for i in range(retries):
                if (i==0):
                    print("Morning Report")
                else:
                    print("\nEvening Report")
                print("Generating Library Report...")
                g=gen_and_verify(*args)
                generated=[]
                for i in g:
                    generated.append(i)
                    print(i)
                    
                it=iter(generated)
                print("\nVerified Records:")
                while True:
                    try:
                        print(next(it))
                    except StopIteration:
                        break
                            
                        
              
                        
        return wrapper
    return decorator
    
    
@retry(2)
def gen_and_verify(rep):
    for i in rep.items():
        yield(f"{i[0]} -> {i[1]}")
        
try:
    n=int(input().strip())
    if n<=0:
        raise InvalidBooks("Invalid Number of Books")
    d={}
    for i in range(n):
        key=input().strip()
        val=input()
        d[key]=val
    gen_and_verify(d)
        
except Exception as e:
    print(e)
