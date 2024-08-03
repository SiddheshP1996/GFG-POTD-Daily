# User function Template for python3

class Solution:
    def celebrity(self, mat):
        # Code here
        lengthOfMatrix = len(mat)
        stackOfMatrixItems = [i for i in range(lengthOfMatrix)]
        
        while len(stackOfMatrixItems) > 1:
            pointerOne = stackOfMatrixItems.pop()
            pointerTwo = stackOfMatrixItems.pop()
            
            if mat[pointerOne][pointerTwo] == 1:
                stackOfMatrixItems.append(pointerTwo)
                
            elif mat[pointerOne][pointerTwo] == 0:
                stackOfMatrixItems.append(pointerOne)
                
        stackItemsPop = stackOfMatrixItems.pop()
        
        for i in range(lengthOfMatrix):
            if i != stackItemsPop:
                if mat[stackItemsPop][i] == 1:
                    return -1
                
                elif mat[i][stackItemsPop] == 0:
                    return -1
        else:
            return stackItemsPop
