"""

Problem Statement:

A social media company collects hashtags used in user posts.
Since users may enter hashtags in different letter cases,
the company wants to standardize all hashtags by converting
them to lowercase.

The analytics team also wants to identify all unique hashtags
and determine how many times each hashtag was used.

For consistent reporting, the unique hashtags and frequency
information should be displayed in alphabetical order.

Requirements:
1. Convert all hashtags to lowercase.
2. Identify unique hashtags.
3. Count the frequency of each hashtag.
4. Display hashtags in alphabetical order.

Input Format:
First line contains an integer N representing the number of hashtags.

Next N lines contain hashtag names.

Output Format:
Print the list of unique hashtags in alphabetical order.
Print the dictionary containing hashtag frequencies in alphabetical order.

Sample Input:
6
Python
AI
python
ML
AI
Data

Sample Output:
['ai', 'data', 'ml', 'python']
{'ai': 2, 'data': 1, 'ml': 1, 'python': 2}
"""
n=int(input())
l=[input().lower() for i in range(n)]
l2=list({i for i in l})
l2.sort()
freq={}
for h in l2:
    freq[h]=sum(1 for x in l if x==h)
print(l2)
print(freq)
    
