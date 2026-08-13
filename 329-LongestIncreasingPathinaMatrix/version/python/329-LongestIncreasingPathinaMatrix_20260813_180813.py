# Last updated: 8/13/2026, 6:08:13 PM
1class Solution:
2    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3        memo={}
4        r,c=len(matrix),len(matrix[0])
5        count=0
6        def dfs(i,j):
7            if i<0 or i==r or j<0 or j==c:
8                return 0
9            if (i,j) in memo:
10                return memo[(i,j)]
11            directions = [(1,0),(-1,0),(0,1),(0,-1)]
12            ans=1
13            for nr,nl in directions:
14                if (i+nr)<r and (i+nr)>=0 and (j+nl)>=0 and (j+nl)<c and matrix[i+nr][j+nl]>matrix[i][j]:
15                    ans=max(ans,1+dfs(i+nr,j+nl))
16            memo[(i,j)]=ans
17            return ans
18        for i in range(r):
19            for j in range(c):
20                count=max(count,dfs(i,j))
21        return count