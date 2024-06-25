# User function Template for python3

class Solution:
    def buildBalancedTree(self, root):
        # code here
        nodes = self.inorder(root)
        n = len(nodes)
        return self.constructBst(nodes, 0, n - 1)

    def inorder(self, root):
        if root is None:
            return []

        return [*self.inorder(root.left), root.data, *self.inorder(root.right)]

    def constructBst(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(nodes[mid])
        node.left = self.constructBst(nodes, start, mid - 1)
        node.right = self.constructBst(nodes, mid + 1, end)
        return node
