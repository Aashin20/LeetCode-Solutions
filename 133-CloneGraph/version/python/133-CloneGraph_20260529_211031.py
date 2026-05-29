# Last updated: 5/29/2026, 9:10:31 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        oldToNew = {}
13        def dfs(node):
14            if node in oldToNew:
15                return oldToNew[node]
16            copy = Node(node.val)
17            oldToNew[node]=copy
18            for nei in node.neighbors:
19                copy.neighbors.append(dfs(nei))
20            return copy
21        return dfs(node) if node else None