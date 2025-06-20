# Last updated: 6/20/2025, 5:46:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val!=q.val:
                return False
            return same(p.left,q.left) and same(p.right,q.right)
        
        def subroot(root):
            if not root:
                return False
            if same(root,subRoot):
                return True
            return subroot(root.right) or subroot(root.left)
        return subroot(root)