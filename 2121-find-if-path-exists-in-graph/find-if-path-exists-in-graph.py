from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        D=defaultdict(list)
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        seen=set()
        seen.add(source)
        stack=[source]
        while stack:
            node=stack.pop()
            for nei_node in D[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)
        if destination in seen:
            return True
        else:
            return False
        