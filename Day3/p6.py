"""


Problem Statement:

An online coding platform stores participant names and their
contest scores.

To prepare the final leaderboard, the platform should:

1. Accept multiple participant scores.
2. Remove duplicate scores.
3. Arrange scores in descending order.
4. Calculate the total score of unique entries.
5. Generate a contest report object.
6. Display report information in a readable format.
7. Log when report generation starts and ends.
8. Retry report generation two times.

Requirements:
1. Use lists, sets and lambda functions.
2. Use *args to calculate the total score.
3. Use __repr__() to display object information.
4. Use decorators and decorator with arguments.
5. Preserve metadata using functools.wraps.

Input Format:
Number of Participants

Participant Name
Participant Score

Output Format:
Display contest reports for each retry attempt.

Sample Input:
5
Ravi
90
Priya
85
Kiran
90
John
70
David
95

Sample Output:
Attempt 1
Report Generation Started
ContestReport(scores=[95, 90, 85, 70], total=340)
Report Generation Finished

Attempt 2
Report Generation Started
ContestReport(scores=[95, 90, 85, 70], total=340)
Report Generation Finished
"""
from functools import wraps

class ContestReport:
    def __init__(self,scores):
        #self.name=name
        self.scores=scores
    def __repr__(self):
        return f"ContestReport(scores={self.scores}, total={self.total})"
    
    def retry(retries=2):
        def decorator(comp):
            @wraps(comp)
            def wrapper(*args):
                for i in range(retries):
                    try:
                        print(f"Attempt {i+1}")
                        print("Report Generation Started")
                        print(comp(*args))
                        print("Report Generation Finished")
                    except Exception as e:
                        print(e)
                
            return wrapper
        return decorator
        
    @retry(2)
    def comp(self):
        scores=list(self.scores)
        removed_dup=list({i for i in scores})
        removed_dup.sort(key=lambda x:x,reverse=True)
        self.scores=removed_dup
        self.total=sum(removed_dup)
        return repr(self)
        
    
    
    
        
n=int(input())
scores=[]
names=[]
for i in range(n):
    names.append(input())
    score=int(input())
    scores.append(score)
c=ContestReport(scores)
c.comp()



