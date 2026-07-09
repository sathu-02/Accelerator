"""

Problem Statement:

Given a string, identify all unique characters and
store the positions at which each character appears.

Input Format:
A string

Output Format:
Dictionary containing character positions.

Sample Input:
banana

Sample Output:
{'b': [0], 'a': [1, 3, 5], 'n': [2, 4]}
"""
s=input()
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
d={}
for ch in l:
    d[ch]=[]
    for i in range(len(s)):
        if ch==s[i]:
            d[ch].append(i)
print(d)
    
    
