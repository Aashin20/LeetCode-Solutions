# Last updated: 7/16/2025, 11:44:52 PM
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt1 = sum(1 for x in nums if x % 2 == 0)
        cnt2 = sum(1 for x in nums if x % 2 == 1)

        eve = odd = 0
        for x in nums:
            if x % 2 == 0:
                eve = max(eve, odd + 1)
            else:
                odd = max(odd, eve + 1)

        return max(cnt1, cnt2, eve, odd)