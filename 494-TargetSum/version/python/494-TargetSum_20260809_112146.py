# Last updated: 8/9/2026, 11:21:46 AM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        dp={}
4        def target_sum(i,summ):
5            if i==len(nums): 
6                return 1 if summ==target else 0
7            if (i,summ) in dp: return dp[(i,summ)]
8            val=target_sum(i+1,summ+nums[i])+target_sum(i+1,summ-nums[i])
9            dp[(i,summ)]=val
10            return val
11        return target_sum(0,0)