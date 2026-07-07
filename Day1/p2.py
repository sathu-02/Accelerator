"""
Problem Statement:
Given the ages of students, print only the ages of students eligible
to vote (age >= 18) using list comprehension.

Input Format:
Space-separated integers representing ages.

Output Format:
Print the list of eligible ages.

Sample Input:
16 20 18 15 22

Sample Output:
[20, 18, 22]
"""

ages=list(map(int, input().split()))
l=list(filter(lambda x:x>=18,ages))
print(l)
