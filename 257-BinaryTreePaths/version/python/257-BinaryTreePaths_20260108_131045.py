# Last updated: 1/8/2026, 1:10:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
9        ans = []
10        def dfs(root,path):
11            if not root:
12                return None
13            if not root.left and not root.right:
14                path.append(str(root.val))
15                ans.append('->'.join(path))
16                path.pop()
17                return 
18            path.append(str(root.val))
19            dfs(root.left,path)
20            dfs(root.right,path)
21            path.pop()
22        
23        dfs(root,[])
24        return ans
25
26            
27