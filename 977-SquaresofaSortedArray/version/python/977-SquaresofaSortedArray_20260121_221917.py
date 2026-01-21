# Last updated: 1/21/2026, 10:19:17 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        for i in range(len(nums)):
4            nums[i]=nums[i]*nums[i]
5            
6        nums.sort()
7        return nums