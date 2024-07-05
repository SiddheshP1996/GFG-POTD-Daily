# User function Template for python3

def traverse(root, lines, currentRoot):
    if root.left:
        lines[0] = min(lines[0], currentRoot - 1)
        traverse(root.left, lines, currentRoot - 1)
    if root.right:
        lines[1] = max(lines[1], currentRoot + 1)
        traverse(root.right, lines, currentRoot + 1)

# Function to find the vertical width of a Binary Tree.
def verticalWidth(root):
    # Code here
    if not root:
        return 0
    lines = [0,0]
    traverse(root, lines, 0)
    return 1 + lines[1] - lines[0]
