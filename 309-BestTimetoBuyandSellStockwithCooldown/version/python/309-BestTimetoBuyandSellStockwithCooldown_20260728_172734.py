# Last updated: 7/28/2026, 5:27:34 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        dp={}
4
5        def dfs(i,buying):
6            if i>=len(prices):
7                return 0
8            if (i,buying) in dp:
9                return dp[(i,buying)]
10            cooldown=dfs(i+1,buying)
11            if buying:
12                buy=dfs(i+1,not buying)-prices[i]
13                dp[(i,buying)] = max(buy,cooldown)
14            else:
15                sell=dfs(i+2,not buying) + prices[i]
16                dp[(i,buying)] = max(sell,cooldown)
17            return dp[(i,buying)]
18        return dfs(0,True)
19