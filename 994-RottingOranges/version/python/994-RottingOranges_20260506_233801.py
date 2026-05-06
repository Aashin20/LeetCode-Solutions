# Last updated: 5/6/2026, 11:38:01 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        q = deque()
4        time,fresh = 0,0
5        ROWS,COLS = len(grid),len(grid[0])
6        for r in range(ROWS):
7            for c in range(COLS):
8                if grid[r][c] == 1:
9                    fresh+=1
10                elif grid[r][c] == 2:
11                    q.append([r,c])
12        
13        directions = [[0,1],[1,0],[0,-1],[-1,0]]
14        while q and fresh>0:
15            for i in range(len(q)):
16                r,c = q.popleft()
17                for dr,dc in directions:
18                    row,col = dr+r,dc+c
19                    if (row<0 or row == ROWS or col<0 or col==COLS or grid[row][col]!=1):
20                        continue
21                    grid[row][col]=2
22                    q.append([row,col])
23                    fresh-=1
24            time+=1
25        return time if fresh==0 else -1
26