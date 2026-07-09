"""

Problem Statement:

A DNA sequence contains characters A, T, G and C.

Create a class that stores the sequence using a constructor and
displays:

1. Length of sequence
2. Count of A
3. Count of G

Input Format:
DNA Sequence

Output Format:
Length
Count of A
Count of G

Sample Input:
ATGCGATAA

Sample Output:
9
4
2
"""
class DNA:
    def __init__(self,dna):
        self.length=len(dna)
        self.a_count=sum(1 for ch in dna.lower() if ch=='a')
        self.g_count=sum(1 for ch in dna.lower() if ch=='g')
    def __str__(self):
        return f"{self.length}\n{self.a_count}\n{self.g_count}"
        
dna=DNA(input())
print(dna)
