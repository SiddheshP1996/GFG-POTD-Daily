#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest (self, arr, target):
        # Your Code Here
        diff, result, n = float('inf'), 0, len(arr)
            
        arr.sort()
        for i in range(n):
            low, high = i + 1, n - 1
            while low < high:
                sumation = arr[i] + arr[low] + arr[high]
                if sumation == target:
                    return sumation
                    
                if abs(sumation - target) < diff:
                    diff = abs(sumation - target)
                    result = sumation 
                elif abs(sumation - target) == diff:
                    result = max(result, sumation)
                
                if sumation > target:
                    high -= 1
                else:
                    low += 1
        return result
