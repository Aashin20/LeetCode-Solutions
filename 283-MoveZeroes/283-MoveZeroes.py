# Last updated: 6/14/2025, 10:33:23 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        return nums
                
        