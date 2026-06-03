# Last updated: 6/3/2026, 11:02:33 AM
1import heapq
2class Solution:
3    def lastStoneWeight(self, stones: List[int]) -> int:
4        heap=[-i for i in stones]
5        heapq.heapify(heap)
6        while heap:
7            if len(heap)==1:
8                return -heap[0]
9            x=-heapq.heappop(heap)
10            y=-heapq.heappop(heap)
11          
12            if x==y:
13                continue
14            else:
15                heapq.heappush(heap,-(x-y))
16        return 0