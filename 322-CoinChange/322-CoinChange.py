# Last updated: 6/14/2025, 10:33:22 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0]*(amount+1)

        for i in range(1,amount+1):
            minn = float('inf')

            for coin in coins:
                diff = i-coin
                if diff<0:
                    break
                
                minn = min(minn,dp[diff]+1)

            dp[i]=minn
        
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1