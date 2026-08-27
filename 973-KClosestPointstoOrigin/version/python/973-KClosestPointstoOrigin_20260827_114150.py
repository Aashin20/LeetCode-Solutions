# Last updated: 8/27/2026, 11:41:50 AM
1import heapq
2class Solution:
3    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
4        heap=[]
5        ans=[]
6        def euclidean(x,y):
7            return ((x-0)*(x-0))+((y-0)*(y-0))
8        for x,y in points:
9            distance=euclidean(x,y)
10            heapq.heappush(heap,[distance,x,y])
11        while k!=0:
12            d,a,b=heapq.heappop(heap)
13            ans.append([a,b])
14            k-=1
15        return ans