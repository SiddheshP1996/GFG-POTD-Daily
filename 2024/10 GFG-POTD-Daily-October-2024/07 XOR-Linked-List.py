# User function Template for python3

def insert(head, data):
    node = Node(data)
    if head == None:
        head = node
    else:
        node.npx = head
        head = node
    return head

def getList(head):
    accessList = []
    while head:
        accessList.append(head.data)
        head = head.npx
    return accessList
