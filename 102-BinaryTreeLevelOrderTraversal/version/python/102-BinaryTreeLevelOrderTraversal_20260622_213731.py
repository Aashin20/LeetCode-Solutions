# Last updated: 6/22/2026, 9:37:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        q=deque()
10        q.append(root)
11        ans=[]
12        if not root: return []
13        while q:
14            n=len(q)
15            level=[]
16            for i in range(n):
17                root=q.popleft()
18                level.append(root.val)
19                if root.left: q.append(root.left)
20                if root.right: q.append(root.right)
21            ans.append(level)
22        return ans
23