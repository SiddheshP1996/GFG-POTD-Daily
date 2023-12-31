# User function Template for python3

class Solution:
    def __init__(self):
        self.a = None

    def findString(self, N, K):

        def dfs(n, k, string, results):
            # Base case: if n becomes 0, add the string to the answer set
            if n == 0:
                results.add(string)
                return results

            # Recursive case: explore all possibilities for the next digit
            for i in range(k):
                results = dfs((n - 1), k, (string + str(i)), results)

            return results

        def find(elements, string):
            visits.add(elements)

            # Check if all possible combinations have been visited
            if len(visits) == (K ** N):
                self.a = string
                return True

            # Explore neighbors in the graph
            for y in graph[elements]:
                if y not in visits and find(y, (string + y[-1])):
                    return True

            visits.remove(elements)
            return False

        results = set()
        results = dfs(N, K, '', results)

        # Build a graph based on common suffixes in the answer set
        graph = {}
        for i in results:
            for z in range(K):
                elements = i[1:] + str(z)
                if elements in results and elements != i:
                    if i in graph:
                        graph[i].append(elements)
                    else:
                        graph[i] = [elements]

        visits = set()

        # Start the search from each element in the answer set
        for i in results:
            if find(i, i):
                return self.a

        return self.a
