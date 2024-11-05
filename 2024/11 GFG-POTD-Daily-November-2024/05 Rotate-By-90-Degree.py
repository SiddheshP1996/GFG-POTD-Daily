# User function Template for python3

def rotate(mat): 
    # Code here
    arrOne = []
    for i in range(len(mat)):
        arrTwo = []
        for j in range(len(mat) - 1, -1, -1):
            arrTwo.append(mat[j][i])
        arrOne.append(arrTwo)
    mat[:] = arrOne
