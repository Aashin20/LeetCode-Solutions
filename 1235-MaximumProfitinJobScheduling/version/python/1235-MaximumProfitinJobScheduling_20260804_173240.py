# Last updated: 8/4/2026, 5:32:40 PM
1class Solution:
2    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
3        rides=sorted(rides)
4        memo={}
5        def dfs(i):
6            if i==len(rides): return 0
7            if i in memo: return memo[i]
8            res=dfs(i+1)
9            j=bisect.bisect_left(rides,[rides[i][1],-1,-1])
10            res=max(res,(rides[i][1]-rides[i][0])+rides[i][2]+dfs(j))
11            memo[i]=res
12            return res
13        return dfs(0)