# Your task is to complete this function

class Solution:
    def matrixDiagonally(self, mat):
        # Code here
        x, y = 0, 0
        n = len(mat)
        result = []
        addX, addY = -1, 1
        while 0 <= x < n and 0 <= y < n:
            result.append(mat[x][y])
            while 0 <= x + addX < n and 0 <= y + addY < n:
                x += addX
                y += addY
                result.append(mat[x][y])
            if (x == 0 or x == n - 1) and (0 <= y < (n - 1)):
                y += 1
            else:
                x += 1
            addX, addY = addY, addX
        return result
