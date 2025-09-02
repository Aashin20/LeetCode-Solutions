# Last updated: 9/2/2025, 4:47:10 PM
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        l=0
        count = 1
        for r in range(len(nums)):
            if r>0 and nums[r-1]+1==nums[r]:
                count+=1
            if r-l+1>k:
                if nums[l]+1 == nums[l+1]:
                    count-=1
                l+=1
            if r-l+1==k:
                if count==k:
                    result.append(nums[r])
                else:
                    result.append(-1)
        return result
            