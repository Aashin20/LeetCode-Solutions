# Last updated: 6/14/2025, 10:32:06 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = 0 
        suffix = sum(nums)
        ans = []
        for x in nums: 
            prefix += x
            ans.append(abs(prefix - suffix))
            suffix -= x
        return ans 