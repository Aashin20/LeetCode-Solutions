# Last updated: 6/23/2026, 11:26:43 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        count=0
10        stk=[(root,float('-inf'))]
11        while stk:
12            node,largest=stk.pop()
13            if node.val>=largest:
14                count+=1
15            largest=max(largest,node.val)
16            if node.left: stk.append((node.left,largest))
17            if node.right: stk.append((node.right,largest))
18        return count