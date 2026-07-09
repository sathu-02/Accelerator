"""

Problem Statement:

A cyber security company wants to analyze passwords created
by users.

For each password:
1. Determine its length.
2. Count the number of vowels present.
3. Display passwords sorted according to their length.

Requirements:
1. Read multiple passwords.
2. Analyze each password.
3. Display password information in ascending order of length.

Input Format:
First line contains an integer N representing the number of passwords.

Next N lines contain password strings.

Output Format:
Display a list containing:
(Password, Length, Number of Vowels)

Sample Input:
3
Python123
Admin@456
AI2025

Sample Output:
[('AI2025', 6, 2), ('Python123', 9, 1), ('Admin@456', 9, 3)]
"""
class Password:
    def __init__(self,p):
        self.p=p
        self.length=len(p)
        self.vow=sum(1 for ch in p.lower() if ch in "aeiou")
n=int(input())
passwords=[]
for i in range(n):
    pwd=Password(input())
    passwords.append(pwd)
    
passwords.sort(key=lambda x:x.length)
res=[(pwd.p, pwd.length, pwd.vow) for pwd in passwords]
print(res)
    
