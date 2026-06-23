# Last updated: 6/23/2026, 3:48:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        summ=[root.val]
10        def dfs(node):
11            if not node:
12                return 0
13            left_sum=max(0,dfs(node.left))
14            right_sum=max(0,dfs(node.right))
15            summ[0]=max(summ[0],node.val+left_sum+right_sum)
16            return node.val+max(left_sum,right_sum)
17        dfs(root)
18        return summ[0]