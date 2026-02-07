# Last updated: 2/7/2026, 3:49:01 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        prev=cost[0]
4        cur=cost[1]
5        temp=0
6        for i in range(2,len(cost)):
7            temp=cur
8            cur = min(prev,cur)+cost[i]
9            prev=temp
10        return min(prev,cur)