# Last updated: 8/1/2025, 9:49:34 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num=float('inf')
        profit=0
        for i in prices:
            min_num=min(min_num,i)
            profit=max(profit,i-min_num)
        return profit