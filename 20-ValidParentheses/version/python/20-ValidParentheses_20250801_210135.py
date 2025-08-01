# Last updated: 8/1/2025, 9:01:35 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        cur_sum=0
        for i in nums:
            cur_sum+=i
            max_sum=max(max_sum,cur_sum)
            if cur_sum<0:
                cur_sum=0    
        return max_sum