# Last updated: 1/5/2026, 1:32:29 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        h={}
4        for i in range(len(nums)):
5            h[nums[i]]=i
6        for i in range(len(nums)):
7            y=target-nums[i]
8            if y in h and h[y]!=i:
9                return [i,h[y]]