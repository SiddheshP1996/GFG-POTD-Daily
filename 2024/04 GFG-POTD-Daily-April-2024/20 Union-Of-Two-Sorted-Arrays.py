# User function Template for python3

class Solution:
    
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, arr1, arr2, n, m):
        """
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        """
        # Code here
        return list(sorted(set(arr1).union(set(arr2))))
