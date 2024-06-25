# User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here

        """
        Solution 1
        """
        arr = []

        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            arr.append(root.data)
            inOrder(root.right)

        def binST():
            left = 0
            right = len(arr) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= x:
                    ans = arr[mid]
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        inOrder(root)
        return binST()

        """
        Solution 2
        """

        # res = -1
        # while root is not None:
        #     if root.data <= x:
        #         res = root.data
        #         root = root.right
        #     else:
        #         root = root.left
        # return res
