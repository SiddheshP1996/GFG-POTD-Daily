# User function Template for python3

from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # Code here
        meetingList = []
        
        for i in range(N):
            meetingList.append([S[i], F[i], i + 1])
            
        # Sorting the list according to end time(F[i]) of meeting
        meetingList.sort(key = lambda x: x[1])
        
        result = [meetingList[0][2]]
        endResult = meetingList[0][1]
        
        for i in range(1, len(meetingList)):
            
            if meetingList[i][0] > endResult:
                
                result.append(meetingList[i][2])
                endResult = meetingList[i][1]
            
        result.sort()
        return result
