# Last updated: 8/1/2025, 7:52:12 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                nums[j]=nums[i]
                j+=1
        return j
