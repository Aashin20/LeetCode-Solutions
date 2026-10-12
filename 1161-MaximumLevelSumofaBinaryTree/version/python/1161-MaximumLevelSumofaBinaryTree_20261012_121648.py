# Last updated: 10/12/2026, 12:16:48 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: TreeNode | None) -> int:
9        if not root:
10            return []
11        q=deque([root])
12        level=1
13        ans=0
14        max_sum=float('-inf')
15        while q:
16            cur=0
17            n=len(q)
18            for i in range(n):
19                node=q.popleft()
20                cur+=node.val
21                if node.left: q.append(node.left)
22                if node.right: q.append(node.right)
23            if cur>max_sum:
24                max_sum=cur
25                ans=level
26            level+=1
27        return ans