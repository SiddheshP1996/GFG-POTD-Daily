# User function Template for python3

"""
class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None
"""

class Solution:
    def constructLinkedMatrix(self, mat):
        # Your code goes here
        for i in range(len(mat)):
            for j in range(len(mat)):
                mat[i][j] = Node(mat[i][j])
                if j != 0:
                    mat[i][j - 1].right = mat[i][j]
                if i != 0:
                    mat[i - 1][j].down = mat[i][j]
        return mat[0][0]
