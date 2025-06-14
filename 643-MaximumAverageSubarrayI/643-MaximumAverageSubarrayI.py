# Last updated: 6/14/2025, 10:33:04 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        cur_sum=0
        for i in range(k):
            cur_sum+=nums[i]
        max_avg=cur_sum/k

        for i in range(k,n):
            cur_sum+=nums[i]
            cur_sum-=nums[i-k]
            avg_sum=cur_sum/k
            max_avg=max(max_avg,avg_sum)
        return max_avg