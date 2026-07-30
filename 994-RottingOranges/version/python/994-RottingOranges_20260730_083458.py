# Last updated: 7/30/2026, 8:34:58 AM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        fresh=0
4        q=deque()
5        time=0
6        ROWS,COLS=len(grid),len(grid[0])
7        for i in range(ROWS):
8            for j in range(COLS):
9                if grid[i][j]==1:
10                    fresh+=1
11                elif grid[i][j]==2:
12                    q.append((i,j))
13        dir=[(0,1),(1,0),(-1,0),(0,-1)]
14        while q and fresh:
15            n=len(q)
16            for x in range(n):
17                i,j=q.popleft()
18                for dirR,dirL in dir:
19                    r,c=i+dirR,j+dirL
20                    if (r<0 or r==ROWS or c<0 or c==COLS or grid[r][c]!=1):
21                        continue
22                    fresh-=1
23                    grid[r][c]=2
24                    q.append((r,c))
25            time+=1
26        return time if fresh==0 else -1