# Last updated: 12/27/2025, 8:06:05 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        queue = deque([root])
12        ans=[]
13        while queue:
14            row_max = queue[0].val
15            n=len(queue)
16            for i in range(n):
17                node = queue.popleft()
18                row_max=max(row_max,node.val)
19                if node.left: queue.append(node.left)
20                if node.right: queue.append(node.right)
21            ans.append(row_max)
22        return ans