# User function Template for python3

class Solution:
    def bottomView(self, root):
        # Code here
        horizontalDistanceMap = {}
        def walk(n, level=0, position=0):
            if not n:
                return
            walk(n.left, level + 1, position - 1)
            if position not in horizontalDistanceMap \
                or horizontalDistanceMap[position][1] <= level:
                    horizontalDistanceMap[position] = (n.data, level)
            walk(n.right, level + 1, position + 1)

        walk(root)
        return [horizontalDistanceMap[k][0] \
            for k in sorted(horizontalDistanceMap)]
