# Last updated: 2/9/2026, 12:51:19 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced=[True]
10
11        def height(root):
12            if not root:
13                return 0
14            left=height(root.left)
15            if balanced[0] is False:
16                return 0
17            right=height(root.right)
18            if abs(left-right)>1:
19                balanced[0]=False
20                return 0
21            return 1+max(left,right)
22        height(root)
23        return balanced[0]