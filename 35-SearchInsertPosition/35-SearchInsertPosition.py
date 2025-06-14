# Last updated: 6/14/2025, 10:34:14 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L<=R:
            M=(L+R)//2
            if nums[M]==target:
                return M
            elif nums[M]>target:
                R=M-1
            else:
                L=M+1
        return L

        