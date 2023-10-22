# User function Template for python3

class Solution:
    def colName(self, n):
        # your code here
        listMap = []

        def traverseAlphabets(x):
            if x == 0:
                return
            l = x % 26
            if l == 0:
                listMap.append(26)
                return traverseAlphabets((x // 26) - 1)
            else:
                listMap.append(l)
                return traverseAlphabets((x // 26))

        traverseAlphabets(n)
        listMap.reverse()
        result = [chr(x - 1 + ord('A')) for x in listMap]

        return "".join(result)
