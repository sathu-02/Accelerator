"""

Problem Statement:

Given N words, identify all unique words and display
them in descending order of their length.

Input Format:
First line contains N.
Next N lines contain words.

Output Format:
Sorted list of unique words.

Sample Input:
6
python
java
python
database
sql
machine

Sample Output:
['database', 'machine', 'python', 'java', 'sql']
"""
n=int(input())
l=[input() for i in range(n)]
l2=list({i for i in l})
l2.sort()
l2.sort(key=lambda x:(-len(x),x))
print(l2)
