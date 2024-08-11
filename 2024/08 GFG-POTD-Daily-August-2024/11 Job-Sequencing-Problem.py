# User function Template for python3

"""
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
"""

class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # Code here
        sortedJobs = sorted(Jobs, key=lambda x:x.profit, reverse=True)
        
        timeline = [-1] * n
        totalProfit, jobsDone = 0, 0
        
        for i in sortedJobs:
            
            index = i.deadline - 1
            
            while index >= 0 and timeline[index] != -1: index -= 1
            
            if index >= 0:
                
                timeline[index] = i.id
                totalProfit, jobsDone = totalProfit + i.profit, jobsDone + 1
                
        return [jobsDone, totalProfit]
