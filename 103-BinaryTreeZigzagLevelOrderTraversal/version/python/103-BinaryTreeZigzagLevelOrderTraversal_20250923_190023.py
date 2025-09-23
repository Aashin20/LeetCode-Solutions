# Last updated: 9/23/2025, 7:00:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        res = []
        q.append(root)
        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right:q.append(node.right)
            level = list(reversed(level)) if len(res)%2 else level
            res.append(level)
        return res
