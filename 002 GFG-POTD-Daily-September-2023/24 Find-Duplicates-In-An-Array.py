class Solution:
    def duplicates(self, arr, n):
        # code here
        result = []
        items = [0] * (n + 1)
        for i in range(n):
            items[arr[i]] += 1
        for i in range(len(items)):
            if items[i] > 1:
                result.append(i)
        if len(result) > 0:
            return result
        return [-1]
    