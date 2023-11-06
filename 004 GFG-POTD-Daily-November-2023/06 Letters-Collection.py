# User function Template for python3

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        # code here
        directory = [{-1, 0, 1}, {-2, -1, 0, 1, 2}]
        results = []

        for que in queries:
            h = que[0]
            i = que[1]
            j = que[2]

            s = 0
            for k in directory[h - 1]:
                for l in directory[h - 1]:
                    if (0 <= (i + k) < n) and (0 <= (j + l) < m) and (((k ** 2) + (l ** 2)) > 0) and not (
                            (h == 2) and ((k ** 2) + (l ** 2)) < 4):
                        s = s + mat[i + k][j + l]
            results.append(s)

        return results
