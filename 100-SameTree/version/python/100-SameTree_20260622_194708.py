# Last updated: 6/22/2026, 7:47:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        def same(left,right):
10            if not left and not right:
11                return True
12            if (right and not left) or (left and not right):
13                return False
14            if left.val!=right.val:
15                return False
16            return same(left.left,right.left) and same(left.right,right.right)
17        return same(p,q)