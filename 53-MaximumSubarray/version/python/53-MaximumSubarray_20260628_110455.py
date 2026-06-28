# Last updated: 6/28/2026, 11:04:55 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        res=[0]*len(nums)
7        for i in range(len(nums)):
8            idx=(i+k)%len(nums)
9            res[idx]=nums[i]
10        nums[:]=res
11