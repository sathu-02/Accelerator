"""
Problem Title: User Login Retry System

Problem Statement:

A banking application allows users to retry login attempts
multiple times before blocking access.

The system should retry the login function three times with
a delay of one second between attempts.

Input Format:
User Name

Output Format:
Display login attempts.

Sample Input:
Ravi

Sample Output:
Attempt 1
Login failed for Ravi
Attempt 2
Login failed for Ravi
Attempt 3
Login failed for Ravi
"""
import time

max_retries=3
name=input()
for i in range(max_retries):
    print(f"Attempt {i+1}")
    time.sleep(1)
    print(f"Login failed for {name}")
    

