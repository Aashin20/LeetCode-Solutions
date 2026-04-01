# Last updated: 4/1/2026, 11:13:27 PM
1import heapq
2class Solution:
3    def minimumEffortPath(self, heights: List[List[int]]) -> int:
4        ROWS,COL = len(heights),len(heights[0])
5        min_heap = [[0,0,0]]
6        visit = set()
7        directions = [[0,1],[0,-1],[1,0],[-1,0]]
8        while min_heap:
9            diff,r,c = heapq.heappop(min_heap)
10            if (r,c) in visit:
11                continue
12            visit.add((r,c))
13            if (r,c) == (ROWS-1,COL-1):
14                return diff
15            for dr,dc in directions:
16                newR,newC = r+dr,c+dc
17                if (newR==ROWS or newC==COL or newR < 0 or newC<0 ):
18                    continue
19                newDiff = max(diff,abs(heights[r][c]-heights[newR][newC]))
20                heapq.heappush(min_heap,[newDiff,newR,newC])
21            
22            
23