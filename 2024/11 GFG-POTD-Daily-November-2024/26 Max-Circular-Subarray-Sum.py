# User function Template for python3

# Complete this function
# Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    # Your code here
    sumOne, sumTwo = 0, 0
    maxSum, minSum = float('-inf'), float('inf')
    total, n = 0, len(arr)
    for a in arr:
        total += a
        sumOne += a
        maxSum = max(maxSum,sumOne)
        sumOne = max(sumOne,0)
        sumTwo += a
        minSum = min(minSum,sumTwo)
        sumTwo = min(sumTwo,0)
    return maxSum if total == minSum else max(maxSum, total - minSum)
