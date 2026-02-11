# Last updated: 2/11/2026, 11:33:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        def dfs(root):
10            if not root:
11                return [0,0]
12            leftPair = dfs(root.left)
13            rightPair = dfs(root.right)
14            withRoot = root.val + leftPair[1] + rightPair[1]
15            withoutRoot = max(leftPair) + max(rightPair)
16            return [withRoot,withoutRoot]
17        return max(dfs(root))