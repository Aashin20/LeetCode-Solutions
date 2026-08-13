# Last updated: 8/13/2026, 6:14:23 PM
1class Solution:
2    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3        memo={}
4        r,c=len(matrix),len(matrix[0])
5        count=0
6        directions = [(1,0),(-1,0),(0,1),(0,-1)]
7        def dfs(i,j):
8            if (i,j) in memo:
9                return memo[(i,j)]
10            ans=1
11            for nr,nl in directions:
12                if (i+nr)<r and (i+nr)>=0 and (j+nl)>=0 and (j+nl)<c and matrix[i+nr][j+nl]>matrix[i][j]:
13                    ans=max(ans,1+dfs(i+nr,j+nl))
14            memo[(i,j)]=ans
15            return ans
16        for i in range(r):
17            for j in range(c):
18                count=max(count,dfs(i,j))
19        return count