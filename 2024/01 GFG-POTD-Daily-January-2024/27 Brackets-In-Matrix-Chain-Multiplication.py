# User function Template for python3

import math

class Solution:
    def matrixChainOrder(self, p, n):
        # Code here
        infinite_num = math.inf
        making_cost = [[infinite_num for num in range(n)] for num in range(n)]
        bracket = [['' for num in range(n)] for num in range(n)]

        for i in range(n - 1):
            making_cost[i][i + 1] = 0
            bracket[i][i + 1] = chr(ord('A') + i)

        for outer_items in range(2, n):
            for inner_items in range(n - outer_items):
                x = outer_items + inner_items
                for num in range(inner_items + 1, n):  # Fix: range(j+1, n)
                    if making_cost[inner_items][x] > making_cost[inner_items][num] + making_cost[num][x] + p[inner_items] * p[x] * p[num]:
                        making_cost[inner_items][x] = making_cost[inner_items][num] + making_cost[num][x] + p[inner_items] * p[x] * p[num]
                        bracket[inner_items][x] = '(' + bracket[inner_items][num] + bracket[num][x] + ')'

        return bracket[0][n - 1]
