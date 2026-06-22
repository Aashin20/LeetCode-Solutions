# Last updated: 6/22/2026, 5:58:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        largest_diameter=[0]
10        def helper(root):
11            if not root: return 0
12            left_height=helper(root.left)
13            right_height=helper(root.right)
14            diameter=left_height+right_height
15            largest_diameter[0]=max(largest_diameter[0],diameter)
16            return 1+max(left_height,right_height)
17        helper(root)
18        return largest_diameter[0]