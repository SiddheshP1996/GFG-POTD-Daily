# User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # Code here
        start = height[0]
        count = 1
        for i in range(1, len(height)):
            if start < height[i]:
                count += 1
                start = height[i]
        return count
