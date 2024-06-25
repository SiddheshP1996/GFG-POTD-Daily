# User function Template for python3

from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        # Code here
        resultList = []
        valueOfXOR = 0
        for element in reversed(queries):
            if element[0] == 0:
                resultList.append(valueOfXOR ^ element[1])
            else:
                valueOfXOR ^= element[1]
        resultList.append(valueOfXOR)
        return sorted(resultList)
