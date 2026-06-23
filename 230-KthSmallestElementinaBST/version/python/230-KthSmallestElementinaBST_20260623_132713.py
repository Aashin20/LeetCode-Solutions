# Last updated: 6/23/2026, 1:27:13 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        count=[k]
10        ans=[0]
11        def dfs(node):
12            if not node: return
13            dfs(node.left)
14            if count[0]==1:
15                ans[0]=node.val
16            count[0]=count[0]-1
17            if count[0]>0:
18                dfs(node.right)
19        dfs(root)
20        return ans[0]