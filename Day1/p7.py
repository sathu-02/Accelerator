"""

Problem Statement:
Write a function that accepts any number of integers and returns
their sum using *args.

Sample Input:
10 20 30 40

Sample Output:
100
"""

def find_sum(*args):
    return sum(args)

l=list(map(int, input().split()))
res=find_sum(*l)
print(res)
