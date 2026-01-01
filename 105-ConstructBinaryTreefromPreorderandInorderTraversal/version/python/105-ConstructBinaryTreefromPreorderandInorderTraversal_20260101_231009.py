# Last updated: 1/1/2026, 11:10:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        if not preorder or not inorder:
10            return None
11        root = TreeNode(preorder[0])
12        mid = inorder.index(preorder[0])
13        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
14        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
15        return root