# User function Template for python3

import collections


class Solution:
    def printMinNumberForPattern(ob, S):
        # code here
        numbers = [str(i) for i in range(9, 0, -1)]
        backlog = collections.deque()
        results = []
        S = S + S[-1]
        for c in S:
            if c == 'I':
                if len(backlog) > 0:
                    backlog.append(numbers.pop())
                    numbers.append(backlog.popleft())
                    while len(backlog) > 0:
                        results.append(backlog.pop())
                results.append(numbers.pop())
            else:
                backlog.append(numbers.pop())
        while len(backlog) > 0:
            results.append(backlog.pop())
        return "".join(results)
