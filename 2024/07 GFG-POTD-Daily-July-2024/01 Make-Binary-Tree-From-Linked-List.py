# User function Template for python3

"""
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""

#Function to make binary tree from linked list.
def convert(head):
    # code here
    a = []
    currentHead = head
    n = 0
    while currentHead != None:
        a.append(currentHead.data)
        currentHead = currentHead.next
        n += 1
        
    def buildTree(i):
        if i >= n:
            return
        newNode = Tree(a[i])
        left = buildTree(2 * i + 1)
        right = buildTree(2 * i + 2)
        newNode.left = left
        newNode.right = right
        return newNode
        
    root = buildTree(0)
    return root
