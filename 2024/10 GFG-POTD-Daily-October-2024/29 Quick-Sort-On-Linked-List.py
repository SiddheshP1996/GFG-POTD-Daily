# User function Template for python3

def quickSort(head):
    # Return head after sorting
    def sortHead(startNode, endNode):
        if not startNode or startNode == endNode or startNode.next == endNode:
            return startNode
            
        pivotValue = startNode.data
        dummyNode = Node(0)
        dummyNode.next = startNode
        
        previousNode, currentNode = dummyNode, startNode          
        while currentNode != endNode:
            nextNode = currentNode.next
            if currentNode.data < pivotValue:
                previousNode.next = currentNode.next
                currentNode.next = dummyNode.next
                dummyNode.next = currentNode
            else:
                previousNode = previousNode.next
                
            currentNode = nextNode
        
        startNode.next = sortHead(startNode.next, endNode)
        return sortHead(dummyNode.next, startNode)
    return sortHead(head, None)
