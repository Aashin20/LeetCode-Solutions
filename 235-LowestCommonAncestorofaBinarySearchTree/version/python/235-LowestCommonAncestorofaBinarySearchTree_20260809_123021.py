# Last updated: 8/9/2026, 12:30:21 PM
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
12            if not root: return
13            lca[0]=root
14            if root is p or root is q:
15                return
16            if root.val>p.val and root.val>q.val:
17                search(root.left)
18            elif root.val<p.val and root.val<q.val:
19                search(root.right)
20            else:
21                return
22        search(root)
23        return lca[0]