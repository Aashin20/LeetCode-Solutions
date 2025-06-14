# Last updated: 6/14/2025, 10:33:36 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=sorted(nums)
        return a[-k]