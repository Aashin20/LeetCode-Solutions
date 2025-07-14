# Last updated: 7/15/2025, 1:15:10 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        num=0
        def dfs(i,j):
            if i>=m or i<0 or j>=n or j<0 or grid[i][j]!='1' :
                return
            else:
                grid[i][j]='0'
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i-1,j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    num+=1
                    dfs(i,j)
                else:
                    continue
        return num