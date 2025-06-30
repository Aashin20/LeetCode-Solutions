# Last updated: 6/30/2025, 11:17:25 PM
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num = Counter(nums)
        max_len=0
        for key in num:
            if key+1 in num:
                max_len=max(max_len,num[key]+num[key+1])

        return max_len