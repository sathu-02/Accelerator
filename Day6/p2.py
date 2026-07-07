"""


Problem Statement:

A bank establishes a secure transaction session whenever
a customer performs banking operations.

When the transaction session starts, the system should
automatically establish a secure connection.

After all customer transactions are completed, the system
should automatically terminate the session.

The system should display appropriate messages while
opening and closing the transaction session.

Each customer record contains:

Account Number
Customer Name
Transaction Amount

Store the customer details using a dictionary.

If the number of customer records is less than or equal to zero,
display:

Invalid Number of Customers

If the transaction amount is less than or equal to zero,
display:

Invalid Transaction Amount

Requirements:
1. Create a Context Manager using __enter__() and __exit__().
2. Use the with statement.
3. Store customer records using a dictionary.
4. Display all customer transactions.
5. Validate the transaction amount.

Input Format:
First line contains the number of customers.

Next N sets contain:

Account Number
Customer Name
Transaction Amount

Output Format:

Establishing Secure Banking Session...
Customer Transactions:
ACC101 -> Ravi -> 5000
ACC102 -> Priya -> 3000
Banking Session Closed Successfully

If the number of customers is invalid, display:

Invalid Number of Customers

If the transaction amount is invalid, display:

Invalid Transaction Amount

Sample Input:
2
ACC101
Ravi
5000
ACC102
Priya
3000

Sample Output:
Establishing Secure Banking Session...
Customer Transactions:
ACC101 -> Ravi -> 5000
ACC102 -> Priya -> 3000
Banking Session Closed Successfully

case=1
input=
2
ACC101
Ravi
5000
ACC102
Priya
3000

output=
Establishing Secure Banking Session...
Customer Transactions:
ACC101 -> Ravi -> 5000
ACC102 -> Priya -> 3000
Banking Session Closed Successfully


case=2
input=
1
ACC201
Kiran
15000

output=
Establishing Secure Banking Session...
Customer Transactions:
ACC201 -> Kiran -> 15000
Banking Session Closed Successfully


case=3
input=
3
ACC101
Ravi
1000
ACC102
Anu
2500
ACC103
Rahul
4000

output=
Establishing Secure Banking Session...
Customer Transactions:
ACC101 -> Ravi -> 1000
ACC102 -> Anu -> 2500
ACC103 -> Rahul -> 4000
Banking Session Closed Successfully

case=4
input=
0

output=
Invalid Number of Customers

case=5
input=
-2

output=
Invalid Number of Customers

case=6
input=
2
ACC101
Ravi
-500
ACC102
Priya
3000

output=
Invalid Transaction Amount
"""
class InvalidCustomers(Exception):
    pass
class InvalidAmt(Exception):
    pass

class TransactionSession:
    def __enter__(self):
        print("Establishing Secure Banking Session...")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print("Banking Session Closed Successfully")
        return self
        
def reportCus(d):
    print("Customer Transactions:")
    for i in d.items():
        print(f"{i[0]} -> {i[1][0]} -> {i[1][1]}")
        
try:        
    n=int(input().strip())
    if n<=0:
        raise InvalidCustomers("Invalid Number of Customers")
    cus={}
    for i in range(n):
        acc=input().strip()
        name=input().strip()
        amt=int(input().strip())
        cus[acc]=[name,amt]
    for i in cus.values():
        if i[1]<=0:
            raise InvalidAmt("Invalid Transaction Amount")
    with TransactionSession():
        reportCus(cus)
except Exception as e:
    print(e)
        
