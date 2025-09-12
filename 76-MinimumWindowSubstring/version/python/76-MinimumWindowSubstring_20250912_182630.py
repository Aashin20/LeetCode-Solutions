# Last updated: 9/12/2025, 6:26:30 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minlen = float('inf')
        cur_sum=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while cur_sum>=target:
                minlen = min(minlen,r-l+1)
                cur_sum-=nums[l]
                l+=1
        return 0 if minlen==float('inf') else minlen