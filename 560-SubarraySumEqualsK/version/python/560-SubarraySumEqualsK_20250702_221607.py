# Last updated: 7/2/2025, 10:16:07 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        longest=0
        zeros=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            w=(r-l)+1
            longest=max(longest,w)
        return longest