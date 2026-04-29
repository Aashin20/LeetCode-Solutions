# Last updated: 4/29/2026, 11:48:14 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        m, n = len(grid),len(grid[0])
4        count=0
5        def dfs(i,j):
6            if i>=m or i<0 or j>=n or j<0 or grid[i][j]!='1':
7                return
8            else:
9                grid[i][j]='0'
10                dfs(i+1,j)
11                dfs(i-1,j)
12                dfs(i,j+1)
13                dfs(i,j-1)
14        
15        for i in range(m):
16            for j in range(n):
17                if grid[i][j]=='1':
18                    count+=1
19                    dfs(i,j)
20        return count