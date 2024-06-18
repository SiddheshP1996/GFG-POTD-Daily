# User function template for Python

class Solution:
    def rectanglesInCircle(self, r):
        # Code here
        count = 0
        for i in range(1, 2 * r):
            for j in range(1, 2 * r):
                if(i ** 2 <= 4 * r * r - j ** 2):
                    count += 1
        return count
