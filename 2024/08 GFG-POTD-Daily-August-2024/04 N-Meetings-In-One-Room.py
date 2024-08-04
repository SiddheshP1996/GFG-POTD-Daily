# User function Template for python3

class Solution:
    
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # Code here
        room_meetings = [(end[i], start[i]) for i in range(n)]
        
        room_meetings.sort(key=lambda x: x[0])
        
        numberOfMeetingCount = 0
        lastEndTime = -1
        
        for meeting in room_meetings:
            currentEndTime, currentStartTime = meeting
            
            if currentStartTime > lastEndTime:
                numberOfMeetingCount += 1
                lastEndTime = currentEndTime
        
        return numberOfMeetingCount
