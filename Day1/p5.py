"""

Problem Statement:
Electricity costs Rs.8 per unit. Given units consumed by households,
calculate the bill amount using lambda and map().

Input Format:
Space-separated integers representing units consumed.

Output Format:
Print the bill amounts.

Sample Input:
100 150 200

Sample Output:
[800, 1200, 1600]
"""

l=list(map(int, input().split()))
res=list(map(lambda x:x*8,l))
print(res)
