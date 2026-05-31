# Last updated: 5/31/2026, 7:19:26 PM
1from collections import defaultdict
2class Solution:
3    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
4        g = defaultdict(list)
5
6        for a, b in prerequisites:
7            g[a].append(b)
8
9        UNVISITED = 0
10        VISITING = 1
11        VISITED = 2
12
13        states = [UNVISITED] * numCourses
14
15        def dfs(node):
16            if states[node] == VISITED:
17                return True
18
19            if states[node] == VISITING:
20                return False
21
22            states[node] = VISITING
23
24            for nei in g[node]:
25                if not dfs(nei):
26                    return False
27
28            states[node] = VISITED
29            return True
30
31        for i in range(numCourses):
32            if not dfs(i):
33                return False
34
35        return True