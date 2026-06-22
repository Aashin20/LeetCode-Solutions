# Last updated: 6/22/2026, 5:25:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root:
10            return
11        root.left,root.right=root.right,root.left
12        self.invertTree(root.left)
13        self.invertTree(root.right)
14        return root