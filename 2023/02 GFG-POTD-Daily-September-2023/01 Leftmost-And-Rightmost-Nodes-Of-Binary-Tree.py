# User function Template for python3

# User function Template for python3

'''
class Node:
    def _init_(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


def printCorner(root):
    # print corner data, no need to print new line
    # code here
    if not root:
        return

    queue = []
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_nodes = []

        for i in range(level_size):
            node = queue.pop(0)

            if i == 0:
                level_nodes.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_size > 1:
            level_nodes.append(node.data)

        print(*level_nodes, end=" ")