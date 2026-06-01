# Last updated: 6/1/2026, 10:00:38 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        g=defaultdict(list)
4        ans=[]
5        for a,b in prerequisites:
6            g[a].append(b)
7
8        UNVISITED=0
9        VISITING=1
10        VISITED=2
11        states=[UNVISITED]*numCourses
12        def dfs(node):
13            if states[node]==VISITED: 
14                return True
15            if states[node]==VISITING: return False
16
17            states[node]=VISITING
18            for nei in g[node]:
19                if not dfs(nei):
20                    return False
21            states[node]=VISITED
22            ans.append(node)
23            return True
24        for i in range(numCourses):
25            if not dfs(i):
26                return []
27        return ans