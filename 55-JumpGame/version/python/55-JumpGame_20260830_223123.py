# Last updated: 8/30/2026, 10:31:23 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        target=len(nums)-1
4        for i in range(len(nums)-1,-1,-1):
5            if i+nums[i]>=target:
6                target=i
7        return target==0