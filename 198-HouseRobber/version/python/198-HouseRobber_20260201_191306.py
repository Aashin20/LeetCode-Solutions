# Last updated: 2/1/2026, 7:13:06 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums)<2:
4            return nums[0]
5        dp=[0]*len(nums)
6        dp[0]=nums[0]
7        dp[1]=max(nums[1],nums[0])
8        for i in range(2,len(nums)):
9            summ = nums[i]+dp[i-2]
10            if summ>dp[i-1]:
11                dp[i]=summ
12            else:
13                dp[i]=dp[i-1]
14        return dp[-1]