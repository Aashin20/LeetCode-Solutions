# Last updated: 6/16/2025, 11:41:32 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff=-1
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if j>i and nums[j]>nums[i]:
                    max_diff=max(max_diff,nums[j]-nums[i])
        return max_diff