# Last updated: 6/22/2026, 6:27:18 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced=[True]
10        def height(root):
11            if not root: return 0
12            left_height=height(root.left)
13            right_height=height(root.right)
14            if abs(left_height-right_height)>1:
15                balanced[0]=False
16                return 0
17            return 1+max(left_height,right_height)
18        height(root)
19        return balanced[0]