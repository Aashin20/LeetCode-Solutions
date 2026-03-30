# Last updated: 3/30/2026, 6:01:11 PM
1import heapq
2class Solution:
3    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
4        graph = defaultdict(list)
5        for i in range(len(edges)):
6            graph[edges[i][0]].append((edges[i][1],succProb[i]))
7            graph[edges[i][1]].append((edges[i][0],succProb[i]))
8        visit = set()
9        min_heap = [(-1,start_node)]
10        while min_heap:
11            prob,i = heapq.heappop(min_heap)
12            if i in visit:
13                continue
14            visit.add(i)
15            if i == end_node:
16                return -prob
17            for nei,nei_prob in graph[i]:
18                if nei not in visit:
19                    heapq.heappush(min_heap,(nei_prob*prob,nei))
20        return 0
21