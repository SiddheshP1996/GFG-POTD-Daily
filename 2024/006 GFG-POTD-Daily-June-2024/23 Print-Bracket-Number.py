# User function Template for python3

class Solution:
    def bracketNumbers(self, str):
        # Code here
        result = []
        stack = []
        count = 0
        for i in str:
            if i == '(':
                count+=1
                stack.append(count)
                result.append(count)
            elif i == ')':
                result.append(stack.pop())
        
        return result
