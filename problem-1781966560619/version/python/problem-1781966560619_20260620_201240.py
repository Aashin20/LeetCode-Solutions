# Last updated: 6/20/2026, 8:12:40 PM
1class Solution:
2    def createGrid(self, m: int, n: int) -> list[str]:
3        ans=[]
4        for i in range(m):
5            path=''
6            for j in range(n):
7                if i==0 or j==n-1:
8                    path+='.'
9                else:
10                    path+='#'
11            ans.append(path)
12        return ans