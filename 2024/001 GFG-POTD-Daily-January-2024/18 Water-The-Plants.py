# User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # Code here
        sprinklerArray = []
        for i in range(n):
            if gallery[i] != -1:
                sprinklerArray.append([max(0, i - gallery[i]), min(n - 1, i + gallery[i])])
        sprinklerArray.sort()

        sprinklers = 0
        i = 0
        start_to_sprinkle = 0

        while start_to_sprinkle < n:
            maximumRange = -1
            while i < len(sprinklerArray) and sprinklerArray[i][0] <= start_to_sprinkle:
                maximumRange = max(maximumRange, sprinklerArray[i][1])
                i += 1
            if maximumRange < start_to_sprinkle:
                return -1
            sprinklers += 1
            start_to_sprinkle = maximumRange + 1
        return sprinklers
