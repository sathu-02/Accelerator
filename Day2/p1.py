"""
Problem Statement:

A university stores student records containing student names and marks.
The administration requires the following operations:

1. When a student object is printed, its details should appear in a
   readable format.

2. The number of characters in a student's name should be obtained
   using the built-in len() function.

3. Two students should be considered equal if they have the same marks.

4. One student should be considered smaller than another student if
   his/her marks are lower.

Input Format:
Student1 Name
Student1 Marks
Student2 Name
Student2 Marks

Output Format:
Display both students.
Display the length of the first student's name.
Check whether both students have equal marks.
Check whether the first student has fewer marks than the second student.

Sample Input:
Ravi
85
Priya
92

Sample Output:
Student(name='Ravi', marks=85)
Student(name='Priya', marks=92)
4
False
True



"""
class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def __str__(self):
        return f"Student(name={self.name}, marks={self.marks})"
        
s1_name=input()
s1_marks=int(input())
s2_name=input()
s2_marks=int(input())

s1=Student(s1_name,s1_marks)
s2=Student(s2_name,s2_marks)

print(s1)
print(s2)
print(len(s1.name))
print(s1.marks==s2.marks)
print(s1.marks<s2.marks)


