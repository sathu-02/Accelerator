"""
Problem Statement:

A software company has developed an API service to process customer requests.
Before executing a request, the system performs authentication and validation
to ensure that only authorized users can access the service.

For this application, only two customers, "Ravi" and "Priya", are registered
users of the system. Requests from any other customer should be rejected.

After successful authentication, the request should be validated and then
processed. The development team also wants to preserve the original metadata
of the service function for debugging and documentation purposes.

Design a request processing system using decorators to implement
authentication and validation stages before executing the service function.

Requirements:
1. Use multiple decorators.
2. Preserve the original function metadata using functools.wraps.
3. Execute decorators in chained order.
4. Process requests only for authorized customers ("Ravi" and "Priya").

Input Format:
Customer Name

Output Format:
If the customer is authorized:
    Authentication Successful
    Request Validated
    Processing request for <Customer Name>
    Function Name: process_request

Otherwise:
    Authentication Failed
    Function Name: process_request

Sample Input 1:
Ravi

Sample Output 1:
Authentication Successful
Request Validated
Processing request for Ravi
Function Name: process_request

Sample Input 2:
Priya

Sample Output 2:
Authentication Successful
Request Validated
Processing request for Priya
Function Name: process_request

Sample Input 3:
Kiran

Sample Output 3:
Authentication Failed
Function Name: process_request
"""

from functools import wraps

def authenticate(func):
    @wraps(func)
    def wrapper(name):
        if name in ["Ravi", "Priya"]:
            print("Authentication Successful")
            return func(name)
        else:
            print("Authentication Failed")
    return wrapper

def validate(func):
    @wraps(func)
    def wrapper(name):
        print("Request Validated")
        return func(name)
    return wrapper

@authenticate
@validate
def process_request(name):
    print(f"Processing request for {name}")

name = input()

process_request(name)
print("Function Name:", process_request.__name__)
    
