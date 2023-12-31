# User function Template for python3

class Solution:
    def isRepresentingBST(self, arr, N):
        # code here
        # in InOrder traversal of BST, the elements
        # should be in sorted order.
        for i in range(N - 1):
            if arr[i + 1] < arr[i]:
                return 0
        return 1
