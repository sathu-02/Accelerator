"""
Problem Statement:

A browser stores a website URL. Create a class that initializes
the URL using a constructor and extracts:

1. Protocol
2. Domain Name
3. Top-Level Domain

Input Format:
URL

Output Format:
Protocol
Domain
Extension

Sample Input:
https://www.google.com

Sample Output:
Protocol: https
Domain: google
Extension: com
"""
class URL:
    def __init__(self, url):
        self.url=url
        self.protocol=url.split('://')[0]
        parts=url.split('://')[1]
        self.domain=parts.split('.')[-2]
        self.ext=parts.split('.')[-1]
        
    def __str__(self):
        return f"Protocol: {self.protocol}\nDomain: {self.domain}\nExtension: {self.ext}"
        
u=URL(input())
print(u)
