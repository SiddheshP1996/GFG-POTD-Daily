# User function Template for python3

from typing import List

class Solution:

    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # code here
        if start == end:
            return 0
        q = [start]
        s = set()
        steps = 0

        while len(q) > 0:
            steps += 1
            size = len(q)

            for i in range(size):
                current = q.pop(0)

                for item in arr:
                    newCurrent = current * item % 100000

                    if newCurrent == end:
                        return steps

                    if newCurrent not in s:
                        s.add(newCurrent)
                        q.append(newCurrent)

        return -1