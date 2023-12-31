# User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


class Solution:
    def getCount(self, root, n):
        # code here
        l = [root]
        level = 0
        count = 0

        while len(l) != 0 and root and n > 0:
            level += 1

            for i in range(len(l)):

                if l[i].left is None and l[i].right is None:
                    n -= level
                    count += 1

                    if n < 0:
                        return count - 1
                    elif n == 0:
                        return count
            l = [node for i in l for node in (i.left, i.right) if node is not None]
        return count
