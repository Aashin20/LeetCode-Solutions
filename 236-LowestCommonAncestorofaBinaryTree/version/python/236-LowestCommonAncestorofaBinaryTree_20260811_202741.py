# Last updated: 8/11/2026, 8:27:41 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root, p, q):
10        def dfs(node):
11            if not node:
12                return 0
13            if node == p: return p
14            if node == q: return q
15            left = dfs(node.left)
16            right=dfs(node.right)
17            if left and right: return node
18            if left: return left
19            if right: return right
20            return None
21        return dfs(root)