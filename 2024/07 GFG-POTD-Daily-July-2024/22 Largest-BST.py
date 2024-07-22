# User function Template for python3

class Solution:
    def largestBst(self, root):
        # Your code here
        def execute(node):
            if not node:
                return True, 0, float("inf"), float("-inf")
            
            left, leftSize, leftMin, leftMax = execute(node.left)
            right, rightSize, rightMin, rightMax = execute(node.right)
            
            if left and right and leftMax < node.data < rightMin:
                return True, 1 + leftSize + rightSize, min(leftMin, node.data), max(node.data, rightMax)
            return False, max(leftSize, rightSize), 0, 0
        
        return execute(root)[1]
