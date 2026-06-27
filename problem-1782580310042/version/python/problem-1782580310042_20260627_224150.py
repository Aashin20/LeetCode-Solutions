# Last updated: 6/27/2026, 10:41:50 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        i=0
4        while i!=len(nums)-1:
5            if nums[i]==nums[i+1]:
6                nums.pop(i+1)
7            else:
8                i+=1
9        return len(nums)