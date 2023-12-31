# User function Template for python3

class Solution:
    def minCandy(self, N, ratings):
        # Code here
        # (a % b) * c + b: a = assumed number of candies, b: actual ratings
        modifiedRatings = max(ratings) + 2
        ratings[0] += modifiedRatings

        for i in range(1, N):
            if ratings[i - 1] % modifiedRatings < ratings[i] % modifiedRatings:
                ratings[i] = ((ratings[i-1] // modifiedRatings) + 1) * modifiedRatings + ratings[i]
            else:
                ratings[i] += modifiedRatings
        
                
        candies = ratings[N - 1] // modifiedRatings

        for i in range(N - 2, -1, -1):
            if ratings[i + 1] % modifiedRatings < ratings[i] % modifiedRatings:
                ratings[i] = max((ratings[i + 1] // modifiedRatings) + 1, ratings[i] // modifiedRatings) * modifiedRatings + (ratings[i] % modifiedRatings)
            candies += (ratings[i] // modifiedRatings)
        
        return candies
