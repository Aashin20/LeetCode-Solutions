# Last updated: 2/10/2026, 11:18:21 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        coins.sort()
4        dp = [0]*(amount+1)
5
6        for i in range(1,amount+1):
7            minn = float('inf')
8
9            for coin in coins:
10                diff = i-coin
11                if diff<0:
12                    break
13                
14                minn = min(minn,dp[diff]+1)
15
16            dp[i]=minn
17        
18        if dp[amount]<float('inf'):
19            return dp[amount]
20        else:
21            return -1