# Last updated: 7/3/2025, 2:37:08 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans=ans^i
        return ans