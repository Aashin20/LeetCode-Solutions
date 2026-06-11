# Last updated: 6/11/2026, 1:53:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        left=self.maxDepth(root.left)
12        right=self.maxDepth(root.right)
13        return 1+max(left,right)