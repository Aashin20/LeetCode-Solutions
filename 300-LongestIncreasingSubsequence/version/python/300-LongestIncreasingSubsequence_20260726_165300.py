# Last updated: 7/26/2026, 4:53:00 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        n=len(nums)
4        dp=[1]*n
5        for i in range(1,n):
6            for j in range(i):
7                if nums[i]>nums[j]:
8                    dp[i]=max(dp[i],dp[j]+1)
9        return max(dp)