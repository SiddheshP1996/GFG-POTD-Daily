# User function Template for python3

class Solution:
    def solve(self, column, board, n, result):
        if column == n:
            result.append(board[:])
            
        for row in range(1, n + 1):
            if all(board[item] != row and \
                abs(board[item] - row) != column - item for item in range(column)):
                board[column] = row
                self.solve(column + 1, board, n, result)
    
    def nQueen(self, n):
        # Code here
        result = []
        self.solve(0, [0] * n, n, result)
        return result
