# Last updated: 6/14/2025, 10:33:26 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=set(nums)
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
            else:
                continue