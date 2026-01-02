# Last updated: 1/2/2026, 8:19:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        def dfs(root):
13            if not root:
14                return None
15            leftTail = dfs(root.left)
16            rightTail = dfs(root.right)
17            if root.left:
18                leftTail.right = root.right
19                root.right = root.left
20                root.left = None
21            return rightTail or leftTail or root
22        dfs(root)