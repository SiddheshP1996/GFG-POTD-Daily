# User function Template for python3

class Solution:
    def printAllDups(self, root):
        # Code here
        resultSet = {}
        seen = set()
        def dfs(currentRoot = root):
            if not currentRoot:
                return [-1]
            left = dfs(currentRoot.left)
            right = dfs(currentRoot.right)
            temporary = [currentRoot.data] + left + right
            if tuple(temporary) in seen:
                resultSet[tuple(temporary)] = currentRoot
            else:
                seen.add(tuple(temporary))
            return temporary
        dfs()
        return [resultSet[x] for x in sorted(resultSet)]
