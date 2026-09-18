# Last updated: 9/18/2026, 7:34:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        def same(p,q):
10            if not p and not q:
11                return True
12            if (p and not q) or (q and not p):
13                return False
14            if p.val!=q.val:
15                return False
16            return same(p.left,q.left) and same(p.right,q.right)
17        return same(p,q)