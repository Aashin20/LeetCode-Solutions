# Last updated: 2/1/2026, 7:14:27 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==0:
5            return nums
6        if n==1:
7            return nums[0]
8        dp=[0]*(n+1)
9        dp[0]=nums[0]
10        dp[1]=max(nums[0],nums[1])
11        for i in range(2,n):
12            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
13        return dp[-2]