# User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# Solution 1

from collections import deque

class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def inorder(self, root):
        q, res = deque(), []
        q.append(root)

        while q:
            top = q.popleft()
            res.append(top.data)
            if top.left: q.append(top.left)
            if top.right: q.append(top.right)
        return sorted(res)

    def bst(self, root, ans):
        if root is None: return
        self.bst(root.left, ans)
        root.data = ans.pop(0)
        self.bst(root.right, ans)

    def binaryTreeToBST(self, root):
        # code here
        self.bst(root, self.inorder(root))
        return root


# Solution 2


from collections import deque

class Solution:
    def inorder(self, root):
        q, res, pos, len1 = deque(), [], 0, 1
        q.append(root)

        while pos<len1:
            top = q[pos]
            res.append(top.data)
            if top.left:
                q.append(top.left)
                len1+=1
            if top.right:
                q.append(top.right)
                len1+=1
            pos+=1
        return sorted(res)

    def bst(self, root, ans):
        if root is None: return
        self.bst( root.left,ans)
        root.data = ans.pop(0)
        self.bst(root.right, ans)

    def binaryTreeToBST(self, root):
        self.bst(root, self.inorder(root))
        return root


# Solution 3

class Solution:
    def inorder(self, node, temp):
        if not node: return
        if node.left:self.inorder(node.left, temp)
        temp.append(node.data)
        if node.right:self.inorder(node.right, temp)

    def bst(self, root, ans):
        if root is None: return
        self.bst( root.left,ans)
        root.data = ans.pop(0)
        self.bst(root.right, ans)

    def binaryTreeToBST(self, root):
        temp = []
        self.inorder(root, temp)
        self.bst(root, sorted(temp))
        return root

# Solution 4

class Solution:
    def binaryTreeToBST(self, root):
        # code here
        ans = []
        q = [root]
        while q:
            nq = []
            for e in q:
                ans.append(e.data)
                if e.left:
                    nq.append(e.left)
                if e.right:
                    nq.append(e.right)
            q = nq
        ans.sort()
        p = 0
        def update(n):
            nonlocal p
            if not n:
                return
            update(n.left)
            n.data = ans[p]
            p += 1
            update(n.right)
        update(root)
        return root
