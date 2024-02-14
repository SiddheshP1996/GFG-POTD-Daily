# User function Template for python3

class Solution:
    def criticalConnections(self, v, adj):
        # Code here
        # Function to find critical connections in a graph
        def pointOfArticulation(u):
            # Function to find Articulation Point and critical connections
            low[u] = time[0]
            disc[u] = time[0]
            time[0] += 1
            visitedNode[u] = True
            for v in adj[u]:
                if visitedNode[v] == False:
                    parentNode[v] = u
                    pointOfArticulation(v)
                    
                    low[u] = min(low[u],low[v])
                    
                    if low[v] > disc[u]:
                        result.append(sorted([u, v]))
                        
                elif parentNode[u] != v:
                    low[u] = min(low[u], disc[v])  
        result = []        
        
        # Initializing low, disc, parentNode, time, and visitedNode arrays
        low = [sys.maxsize for itemNode in range(v)]
        disc = [sys.maxsize for itemNode in range(v)]
        parentNode = [-1 for itemNode in range(v)]
        time = [0]
        visitedNode = [False for itemNode in range(v)]
        
        # Calling pointOfArticulation function for each unvisitedNode vertex
        for itemNode in range(v):
            if visitedNode[itemNode] == False:
                pointOfArticulation(itemNode)
        return sorted(result)
