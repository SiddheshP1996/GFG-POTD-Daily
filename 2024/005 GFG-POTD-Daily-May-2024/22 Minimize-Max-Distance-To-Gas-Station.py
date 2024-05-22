# User function Template for python3

class Solution:
    
    def isValid(self, stations, K, distance, n):
        new_stations = 0
        for i in range(1, n):
            new_stations += (stations[i] - stations[i - 1]) // distance
        return new_stations <= K
        
    def findSmallestMaxDist(self, stations, K):
        # Code here
        n = len(stations)
        start = 0
        end = stations[n - 1] - stations[0]
        while end - start > 1e-6:
            mid = start + (end - start) / 2.0
            if self.isValid(stations, K, mid, n):
                end = mid
            else:
                start = mid
        return start + 0.000001
