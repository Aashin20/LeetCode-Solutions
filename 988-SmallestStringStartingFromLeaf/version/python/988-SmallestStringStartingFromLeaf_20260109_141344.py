# Last updated: 1/9/2026, 2:13:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
9        def dfs(root,cur):
10            if not root:
11                return None
12            cur = chr(ord('a')+root.val)+cur
13            if root.left and root.right:
14                return min(dfs(root.left,cur),dfs(root.right,cur))
15            if root.right:
16                return dfs(root.right,cur)
17            if root.left:
18                return dfs(root.left,cur)
19            return cur
20        return dfs(root,"")