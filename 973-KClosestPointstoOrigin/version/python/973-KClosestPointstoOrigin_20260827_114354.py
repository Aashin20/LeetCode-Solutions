# Last updated: 8/27/2026, 11:43:54 AM
1import heapq
2class Solution:
3    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
4        heap=[]
5        for x,y in points:
6            distance=(x*x)+(y*y)
7            heapq.heappush(heap,[-distance,x,y])
8            if len(heap)>k:
9                heapq.heappop(heap)
10        return [[x,y] for dist,x,y in heap]