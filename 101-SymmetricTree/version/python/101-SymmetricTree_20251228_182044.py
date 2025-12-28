# Last updated: 12/28/2025, 6:20:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        def same(p,q):
10            if not p and not q:
11                return True
12            if (p and not q) or (q and not p):
13                return False
14            if p.val!=q.val:
15                return False
16            return same(p.left,q.right) and same(p.right,q.left)
17        return same(root.left,root.right)