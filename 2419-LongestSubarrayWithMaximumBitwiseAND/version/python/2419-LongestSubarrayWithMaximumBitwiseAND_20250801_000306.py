# Last updated: 8/1/2025, 12:03:06 AM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_streak = max(
            len(list(values))
            for key, values in groupby(nums)
            if key == max_val
        )
        return max_streak