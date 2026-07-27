# Last updated: 7/27/2026, 12:06:07 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        memo={(0,0):1}
4        def paths(i,j):
5            if (i,j) in memo:
6                return memo[(i,j)]
7            elif i<0 or j<0 or i==m or j==n:
8                return 0
9            else:
10                val=paths(i,j-1)+paths(i-1,j)
11                memo[(i,j)]=val
12                return val
13        return paths(m-1,n-1)