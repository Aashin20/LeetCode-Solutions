# Last updated: 7/28/2026, 6:20:56 PM
1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        dp={}
4        def count(i,amt):
5            if amt==amount: return 1
6            if amt>amount: return 0
7            if i==len(coins): return 0
8            if (i,amt) in dp:
9                return dp[(i,amt)]
10            else:
11                take=count(i,amt+coins[i])
12                skip=count(i+1,amt)
13                dp[(i,amt)]=take+skip
14                return dp[(i,amt)]
15        return count(0,0)    