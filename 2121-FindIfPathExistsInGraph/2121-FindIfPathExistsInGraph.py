# Last updated: 6/14/2025, 10:32:24 PM
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        D=defaultdict(list)
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        seen=set()
        seen.add(source)
        stack=[source]
        while stack:
            node=stack.pop()
            if node==destination:
                return True
            for nei_node in D[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)
        return False