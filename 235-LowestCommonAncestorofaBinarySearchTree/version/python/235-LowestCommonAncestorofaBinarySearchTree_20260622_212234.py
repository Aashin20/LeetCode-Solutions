# Last updated: 6/22/2026, 9:22:34 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        lca=[root]
11        def search(root):
12            if not root:
13                return
14            lca[0]=root
15            if root is p or root is q:
16                return
17            elif root.val<p.val and root.val<q.val:
18                search(root.right)
19            elif root.val>p.val and root.val>q.val:
20                search(root.left)
21            else:
22                return
23        search(root)
24        return lca[0]