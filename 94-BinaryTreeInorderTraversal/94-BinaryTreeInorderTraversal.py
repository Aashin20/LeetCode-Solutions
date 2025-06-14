# Last updated: 6/14/2025, 10:33:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)
        inorder(root)
        return a
        