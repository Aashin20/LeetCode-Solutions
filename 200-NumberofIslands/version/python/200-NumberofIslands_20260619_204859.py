# Last updated: 6/19/2026, 8:48:59 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        R,C=len(grid),len(grid[0])
4        count=0
5        def capture(r,c):
6            if  r>=R or c>=C or r<0 or c<0 or grid[r][c]!='1':
7                return
8            grid[r][c]='0'
9            capture(r+1,c)
10            capture(r-1,c)
11            capture(r,c+1)
12            capture(r,c-1)
13        for i in range(R):
14            for j in range(C):
15                if grid[i][j]=='1':
16                    count+=1
17                    capture(i,j)
18        return count
19
20        