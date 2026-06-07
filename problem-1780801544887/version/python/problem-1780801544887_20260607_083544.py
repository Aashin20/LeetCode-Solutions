# Last updated: 6/7/2026, 8:35:44 AM
1class Solution:
2    def generateValidStrings(self, n: int, k: int) -> list[str]:
3        ans=[]
4        def dfs(i,prev,cost,cur):
5            if cost>k:
6                return
7            if i==n:
8                ans.append("".join(cur))
9                return
10            cur.append('0')
11            dfs(i+1,0,cost,cur)
12            cur.pop()
13            if prev==0:
14                cur.append('1')
15                dfs(i+1,1,cost+i,cur)
16                cur.pop()
17        dfs(0,0,0,[])
18        return ans