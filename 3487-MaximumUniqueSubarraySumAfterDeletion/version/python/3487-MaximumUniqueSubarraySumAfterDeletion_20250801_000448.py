# Last updated: 8/1/2025, 12:04:48 AM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n < 0 for n in nums):
            return max(nums)
        
        unique = set(nums)
        return sum(n for n in unique if n > 0)