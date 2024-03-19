# User function Template for python3

class Solution:
    def maximumWeight(self, n, edges, q, queries):
        # Code here
        parentArray = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
        def find(n1):
            while (parentArray[n1] != n1):
                parentArray[n1] = parentArray[parentArray[n1]]
                n1 = parentArray[n1]
            return parentArray[n1]
        edges.sort(key = lambda x: x[2], reverse = True)
        queries = sorted(enumerate(queries) , key = lambda x: x[1])
        
        result = [0] * q
        currentIndex = 0
        for index, x in queries:
            while edges and edges[-1][2] <= x :
                node_edge_u, node_edge_v, weight_edge = edges.pop()
                node_edge_u, node_edge_v = find(node_edge_u - 1), find(node_edge_v - 1)
                if node_edge_u != node_edge_v:
                    parentArray[node_edge_v] = node_edge_u 
                    currentIndex += rank[node_edge_u] * rank[node_edge_v]
                    rank[node_edge_u] += rank[node_edge_v]
            result[index] = currentIndex
            
        return result
