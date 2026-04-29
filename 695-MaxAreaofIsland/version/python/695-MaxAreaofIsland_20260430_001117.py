# Last updated: 4/30/2026, 12:11:17 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        m,n = len(grid),len(grid[0])
4        area=0
5        def dfs(i,j):
6            if i>=m or i<0 or j>=n or j<0 or grid[i][j]!=1:
7                return 0
8            grid[i][j]=0
9            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
10        for i in range(m):
11            for j in range(n):
12                if grid[i][j]==1:
13                    area = max(area,dfs(i,j))
14        return area