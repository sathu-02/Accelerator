"""
Problem Statement:

Given N words, convert all words to lowercase and determine
how many times each word appears.

Display the words sorted according to:
1. Frequency (descending)
2. Alphabetical order (ascending) when frequencies are equal.

Input Format:
First line contains an integer N.
Next N lines contain words.

Output Format:
Display a list of tuples containing:
(word, frequency)

Sample Input:
7
Apple
banana
apple
Orange
banana
APPLE
orange

Sample Output:
[('apple', 3), ('banana', 2), ('orange', 2)]
"""
n=int(input())
l=[input().strip().lower() for i in range(n)]
l2=list({i for i in l})
#l2.sort()
l2.sort(key=lambda x:(-l.count(x),x))

res=[]
for i in l2:
    res.append(tuple([i,l.count(i)]))
print(res)
