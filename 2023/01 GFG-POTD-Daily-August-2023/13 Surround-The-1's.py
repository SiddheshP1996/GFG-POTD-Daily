# User function Template for python3

class Solution:
    def Count(self, matrix):
        # Code here
        row_element = len(matrix)
        col_element = len(matrix[0])
        ans = 0
        traverse = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        for i in range(row_element):
            for j in range(col_element):
                if matrix[i][j] == 1:
                    zeros = 0
                    for k in traverse:
                        new_row_element = i + k[0]
                        new_col_element = j + k[1]
                        if 0 <= new_row_element < row_element and new_col_element >= 0 and new_col_element < col_element:
                            if matrix[new_row_element][new_col_element] == 0:
                                zeros += 1
                    if zeros > 0 and zeros % 2 == 0:
                        ans += 1
        return ans
