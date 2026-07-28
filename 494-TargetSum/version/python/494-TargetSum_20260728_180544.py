# Last updated: 7/28/2026, 6:05:44 PM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        dp={}
4        def targetSum(i,total):
5            if i==len(nums):
6                return 1 if total==target else 0
7            if (i,total) in dp:
8                return dp[(i,total)]
9            dp[(i,total)]=targetSum(i+1,total+nums[i])+targetSum(i+1,total-nums[i])
10            return dp[(i,total)]
11        return targetSum(0,0)