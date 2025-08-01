# Last updated: 8/1/2025, 9:00:42 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            cur_sum+=nums[i]
            max_sum=max(max_sum,cur_sum)

            if cur_sum<0:
                cur_sum=0
        return max_sum