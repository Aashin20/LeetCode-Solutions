# Last updated: 12/27/2025, 8:18:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return []
11        queue = deque([root])
12        level_sum = []
13        while queue:
14            level=[]
15            n = len(queue)
16            for i in range(n):
17                node = queue.popleft()
18                level.append(node.val)
19                if node.left: queue.append(node.left)
20                if node.right: queue.append(node.right)
21            level_sum.append(sum(level))
22        max_sum = max(level_sum)
23        return level_sum.index(max_sum)+1
24            
25