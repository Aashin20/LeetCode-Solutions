# Last updated: 5/9/2026, 11:53:35 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        prev=cost[0]
4        cur=cost[1]
5        for i in range(2,len(cost)):
6            temp=min(prev,cur)+cost[i]
7            prev=cur
8            cur=temp
9        return min(prev,cur)
10