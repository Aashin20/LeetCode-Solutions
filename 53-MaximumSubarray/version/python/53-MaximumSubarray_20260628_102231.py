# Last updated: 6/28/2026, 10:22:31 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        cur=0
4        maxx=float('-inf')
5        for i in nums:
6            cur+=i
7            maxx=max(cur,maxx)
8            if cur<0:
9                cur=0
10        return maxx