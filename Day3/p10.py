"""

Problem Statement:

A research organization stores citation counts of published papers.
Duplicate citation counts may exist.

The system should:

1. Remove duplicate citation counts.
2. Calculate the total citation count.
3. Sort citation counts in descending order.
4. Display report information using a class.

Requirements:
1. Use list operations and sets.
2. Use *args to compute total citations.
3. Use lambda while sorting.
4. Display object information using __repr__().

Input Format:
Number of Papers
Citation Counts

Output Format:
ResearchReport(total=?, citations=?)

Sample Input:
6
20
15
20
10
40
15

Sample Output:
ResearchReport(total=85, citations=[40, 20, 15, 10])
"""
class ResearchReport:
    def __init__(self,papers,*args):
        self.papers=papers
        self.args=args
    
        
    def compute_and_sort_citations(self):
        self.total=sum(self.args)
        self.citations=sorted(self.args,key=lambda x:x, reverse=True)
    
    def __repr__(self):
       return f"ResearchReport(total={self.total}, citations={self.citations})"
n=int(input())
l=[int(input()) for i in range(n)]
l2=list({i for i in l})
r=ResearchReport(n,*l2)
r.compute_and_sort_citations()
print(repr(r))
