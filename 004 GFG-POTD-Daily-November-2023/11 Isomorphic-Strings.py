# User function Template for python3

class Solution:

    # Function to check if two strings are isomorphic.
    def areIsomorphic(self, str1, str2):
        if len(str1) != len(str2):
            return False
        map1 = {}
        N = len(str1)
        mapped = set()
        for i in range(N):
            c = str1[i]
            d = str2[i]
            if d not in map1 and c not in mapped:
                map1[d] = c
                mapped.add(c)
        ans = []

        for i in range(N):
            d = str2[i]
            if d in map1:
                ans.append(map1[d])
            else:
                ans.append(d)

        return "".join(ans) == str1
