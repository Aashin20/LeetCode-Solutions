# Last updated: 8/9/2026, 10:26:17 PM
1class Solution:
2    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
3        intervals=sorted(zip(startTime,endTime,profit))
4        memo={}
5        def dfs(i):
6            if i==len(intervals):
7                return 0
8            if i in memo: return memo[i]
9            res=dfs(i+1)
10            val=bisect.bisect_left(intervals,(intervals[i][1],-1,-1))
11            res=max(res,dfs(val)+intervals[i][2])
12            memo[i]=res
13            return res
14        return dfs(0)