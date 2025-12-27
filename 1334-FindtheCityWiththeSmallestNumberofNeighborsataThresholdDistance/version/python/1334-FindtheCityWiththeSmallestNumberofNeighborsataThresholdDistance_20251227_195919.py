# Last updated: 12/27/2025, 7:59:19 PM
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
11        queue = deque()
12        queue.append(root)
13        ans=[]
14        while queue:
15            level=[]
16            n=len(queue)
17            for i in range(n):
18                node = queue.popleft()
19                level.append(node.val)
20                if node.left: queue.append(node.left)
21                if node.right: queue.append(node.right)
22            ans.append(max(level))
23        return ans