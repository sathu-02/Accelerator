"""
Problem Statement:

A university maintains student records in a list.

To search for a particular student mark, two different
search methods are used.

Method 1:
Linear Search

Method 2:
Binary Search

The program should determine whether the given mark is
present using both methods.

Instead of measuring execution time, compare the
performance by counting the number of comparisons
performed by each method.

The search functions should use Python Type Hints.

After searching, display:

• Search Result
• Number of comparisons made by Method 1
• Number of comparisons made by Method 2
• Faster Search Method

Requirements:
-------------
1. Create two search functions.
2. Use Python Type Hints.
3. Method 1 should implement Linear Search.
4. Method 2 should implement Binary Search.
5. Count the number of comparisons performed.
6. Display the faster search method.

Input Format:
-------------
First line contains the number of student marks N.

Next N lines contain the marks.

Last line contains the search key.

Output Format:
--------------
Search Result : Found

Method 1 Comparisons : <count>

Method 2 Comparisons : <count>

Fastest Method : <Method Name>

If the mark is not found:

Search Result : Not Found

Sample Input:
-------------
5
60
75
80
90
95
90

Sample Output:
--------------
Search Result : Found
Method 1 Comparisons : 4
Method 2 Comparisons : 2
Fastest Method : Method 2

Test Cases:
-----------

case=1
input=5
60
75
80
90
95
90

output=
Search Result : Found
Method 1 Comparisons : 4
Method 2 Comparisons : 2
Fastest Method : Method 2

case=2
input=6
10
20
30
40
50
60
25

output=
Search Result : Not Found
Method 1 Comparisons : 6
Method 2 Comparisons : 3
Fastest Method : Method 2

case=3
input=1
100
100

output=
Search Result : Found
Method 1 Comparisons : 1
Method 2 Comparisons : 1
Fastest Method : Both Methods

case=4
input=0

output=
Invalid Number of Students

case=5
input=3
50
-10
80

output=
Invalid Marks
"""

from typing import List, Tuple

class InvalidStudents(Exception):
    pass
class InvalidMarks(Exception):
    pass

def binary_search(key:int,start:int,end:int,arr:List[int],count:int) -> Tuple[int,int]:
    if start>end:
        return (-1,count)
    mid=(start+end)//2
    count+=1
    if arr[mid]==key:
        return (mid, count)
    elif arr[mid]<key:
        start=mid+1
        return binary_search(key,start,end,arr,count)
    elif arr[mid]>key:
        end=mid-1
        return binary_search(key,start,end,arr,count)

def linear_search(arr:List[int],key:int,count:int) -> Tuple[int,int]:
    for i in range(len(arr)):
        count+=1
        if arr[i]==key:
            return (i,count)
    return (-1,count)
        
        

try:
    n:int=int(input().strip())
    if n<=0:
        raise InvalidStudents("Invalid Number of Students")
    arr=[int(input()) for i in range(n)]
    for i in arr:
        if i<0:
            raise InvalidMarks("Invalid Marks")
    key=int(input().strip())
    res1=binary_search(key,0,n-1,arr,0)
    res2=linear_search(arr,key,0)
    
    if res1[0]!=-1 and res2[0]!=-1:
        print(f"Search Result : Found")
    else:
        print(f"Search Result : Not Found")
        
    print(f"Method 1 Comparisons : {res2[1]}")
    print(f"Method 2 Comparisons : {res1[1]}")
    best="Method 2"
    if res1[1]>res2[1]:
        best="Method 1"
    elif res1[1]==res2[1]:
        best="Both Methods"
            
    print(f"Fastest Method : {best}")
    
    
except Exception as e:
    print(e)
            
