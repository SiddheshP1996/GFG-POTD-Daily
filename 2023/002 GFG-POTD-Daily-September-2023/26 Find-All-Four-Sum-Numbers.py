# User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        arr.sort()
        N = len(arr)
        result = []

        for i in range(N - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, N - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                left = j + 1
                right = N - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]
                    if total == k:
                        result.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        right -= 1
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    elif total < k:
                        left += 1
                    else:
                        right -= 1
        return result
