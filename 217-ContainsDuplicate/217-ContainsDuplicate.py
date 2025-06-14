# Last updated: 6/14/2025, 10:33:35 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for x in nums:
            if x in s:
                return True
            else:
                s.add(x)
        return False