# Last updated: 3/29/2026, 11:35:51 PM
1import heapq
2class Solution:
3    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
4        graph = defaultdict(list)
5        for u,v,time in times:
6            graph[u].append((v,time))
7        min_time = {}
8        min_heap = [(0,k)]
9        while min_heap:
10            time,i = heapq.heappop(min_heap)
11            if i in min_time:
12                continue
13            min_time[i] = time
14            for nei,nei_time in graph[i]:
15                if nei not in min_time:
16                    heapq.heappush(min_heap,(time+nei_time,nei))
17        
18        if len(min_time)==n:
19            return max(min_time.values())
20        else:
21            return -1