"""
Problem Statement:

A software company wants to monitor the execution of critical functions
used in its data processing system.

Whenever a function is executed, the monitoring system should:

1. Display a message before the function starts execution.
2. Record the function's execution time.
3. Display a message after the function finishes execution.
4. Preserve the original metadata of the function.

Develop a monitoring system using Python decorators and apply it to a
function that computes the sum of numbers from 1 to N.

Requirements:
1. Use multiple decorators to implement logging and timing features.
2. Preserve the original function metadata.
3. Apply both decorators to the target function.

Input Format:
A single integer N.

Output Format:
Display the start message, computed sum, execution information,
and completion message.

Sample Input:
100000

Sample Output:
Starting function
Sum = 5000050000
Execution Time Recorded
Ending function
"""

from functools import wraps
import time

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting function")
        result = func(*args, **kwargs)
        print("Ending function")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time Recorded")
        return result
    return wrapper

@logger
@timer
def compute_sum(n):
    total = sum(range(1, n + 1))
    print(f"Sum = {total}")

n = int(input())
compute_sum(n)
