# Last updated: 6/23/2026, 12:26:32 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        def valid(node,minn,maxx):
10            if not node: 
11                return True
12            if node.val<=minn or node.val>=maxx:
13                return False
14            return valid(node.left,minn,node.val) and valid(node.right,node.val,maxx)
15        return valid(root,float('-inf'),float('inf'))