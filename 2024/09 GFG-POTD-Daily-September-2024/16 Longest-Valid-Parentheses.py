# User function Template for Python3

class Solution:
    def maxLength(self, str):
        # Code here
        stack = [-1]
        maxLength = 0
        
        for i, char in enumerate(str):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxLength = max(maxLength, i - stack[-1])
                else:
                    stack.append(i)
        
        return maxLength
