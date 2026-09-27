# Last updated: 9/27/2026, 11:52:08 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        d={}
4        for i in range(len(nums)):
5            if nums[i] in d:
6                return [d[nums[i]],i]
7            else:
8                d[target-nums[i]]=i
9            