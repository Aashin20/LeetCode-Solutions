# Last updated: 6/22/2026, 8:20:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        def same(root,subroot):
10            if not root and not subroot:
11                return True
12            if (root and not subroot) or (subroot and not root):
13                return False
14            if root.val!=subroot.val:
15                return False
16            return same(root.left,subroot.left) and same(root.right,subroot.right)
17        
18        def has_subroot(root):
19            if not root: 
20                return False
21            if same(root,subRoot):
22                return True
23            return has_subroot(root.left) or has_subroot(root.right)
24        return has_subroot(root)