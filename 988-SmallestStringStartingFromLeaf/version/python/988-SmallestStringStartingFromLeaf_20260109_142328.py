# Last updated: 1/9/2026, 2:23:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path, small):
            if not node: return 

            path.append(chr(node.val + ord('a')))

            if not node.left and not node.right:
                cur = ''.join(path[::-1])
                small[0] = min(small[0], cur)
            dfs(node.left, path, small)
            dfs(node.right, path, small)
            path.pop()
        small = [chr(ord('z') + 1)]
        dfs(root, [], small)
        return small[0]