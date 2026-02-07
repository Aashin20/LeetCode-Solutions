# Last updated: 2/7/2026, 3:45:54 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n=len(cost)
4        dp=[0]*n
5        dp[0]=cost[0]
6        dp[1]=cost[1]
7        for i in range(2,n):
8            dp[i] = min(dp[i-1],dp[i-2])+cost[i]
9        return min(dp[-1],dp[-2])