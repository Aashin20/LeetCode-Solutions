# Last updated: 9/18/2026, 8:10:06 PM
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
11            if not root: 
12                return 0
13            left_height = helper(root.left)
14            right_height = helper(root.right)
15            diameter = left_height+right_height
16            largest_diameter[0]=max(largest_diameter[0],diameter)
17            return 1+max(left_height,right_height)
18        helper(root)
19        return largest_diameter[0]