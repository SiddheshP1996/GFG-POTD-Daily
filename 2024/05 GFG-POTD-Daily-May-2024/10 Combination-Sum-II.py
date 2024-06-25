# User function Template for python3

class Solution:
    
    def CombinationSum2(self, arr, n, k):
        # Code here
        result = []
        arr.sort()
        
        def execute(index, indexSum, path, result):
            if indexSum == k:
                result.append(path)
            if indexSum > k:
                return 
            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i - 1]:
                    continue
                execute(i + 1, indexSum + arr[i], path + [arr[i]], result)
        execute(0, 0, [], result)
        return result
