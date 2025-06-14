# Last updated: 6/14/2025, 10:31:43 PM
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[0]-nums[-1]), max(abs(x-y) for x, y in pairwise(nums)))
        