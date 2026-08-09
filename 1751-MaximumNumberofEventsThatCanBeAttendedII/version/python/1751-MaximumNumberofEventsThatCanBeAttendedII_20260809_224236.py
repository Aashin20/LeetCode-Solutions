# Last updated: 8/9/2026, 10:42:36 PM
1class Solution:
2    def maxValue(self, events: List[List[int]], k: int) -> int:
3        events.sort()
4        memo={}
5        def dfs(i,k):
6            if i==len(events) or k==0: return 0
7            if (i,k) in memo: return memo[(i,k)]
8            res=dfs(i+1,k)
9            j=bisect.bisect_left(events,[events[i][1]+1,-1,-1])
10            res=max(res,dfs(j,k-1)+events[i][2])
11            memo[(i,k)]=res
12            return res
13        return dfs(0,k)