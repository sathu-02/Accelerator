"""
Problem Statement:
Overload the + operator to add pages of two books.

Input Format:
Pages in first book
Pages in second book

Output Format:
Print total pages.

Sample Input:
100
150

Sample Output:
250
"""
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
        
b1=Book(int(input()))
b2=Book(int(input()))
print(b1+b2)
