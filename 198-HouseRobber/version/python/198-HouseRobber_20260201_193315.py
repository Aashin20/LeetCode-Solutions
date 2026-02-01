# Last updated: 2/1/2026, 7:33:15 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums)<2:
4            return nums[0]
5        def helper(nums):
6            n=len(nums)
7            if n==0:
8                return nums
9            if n==1:
10                return nums[0]
11            dp=[0]*(n+1)
12            dp[0]=nums[0]
13            dp[1]=max(nums[0],nums[1])
14            for i in range(2,n):
15                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
16            return max(dp)
17        return max(helper(nums[1:]),helper(nums[:-1]))