# Last updated: 12/27/2025, 8:37:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_level, level = 1, 1

        maxSum = float('-inf')

        queue = [root]

        while queue:
            level_sum = 0
            next_level = []

            for node in queue:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > maxSum:
                maxSum = level_sum
                max_level = level

            queue = next_level
            level += 1

        return max_level






