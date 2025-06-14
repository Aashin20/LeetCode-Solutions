# Last updated: 6/14/2025, 10:34:34 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]]=i
        for i in range(len(nums)):
            y=target-nums[i]
            if y in h and h[y]!=i:
                return [h[y],i]