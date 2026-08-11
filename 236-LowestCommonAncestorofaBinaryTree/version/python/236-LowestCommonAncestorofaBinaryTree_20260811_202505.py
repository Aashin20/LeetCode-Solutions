# Last updated: 8/11/2026, 8:25:05 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root, p, q):
10
11        def dfs(node):
12            if not node:
13                return None
14
15            if node == p:
16                return p
17
18            if node == q:
19                return q
20
21            left = dfs(node.left)
22            right = dfs(node.right)
23
24            if left and right:
25                return node
26
27            if left:
28                return left
29
30            if right:
31                return right
32
33            return None
34
35        return dfs(root)