# User function Template for python3


# User function Template for python3

class Solution:

    def findNode(self, n, parentNode):
        if parentNode[n] == n:
            return n
        parentNode[n] = self.findNode(parentNode[n], parentNode)
        return parentNode[n]

    def unionOfNode(self, a, b, parentNode):
        x = self.findNode(a, parentNode)
        y = self.findNode(b, parentNode)
        if x != y:
            parentNode[x] = y
            return False
        return True

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        # Code here
        parentNode = list(range(V))

        for i in range(V):
            for j in range(len(adj[i])):
                if i < adj[i][j] and self.unionOfNode(i, adj[i][j], parentNode):
                    return 1
        return 0
