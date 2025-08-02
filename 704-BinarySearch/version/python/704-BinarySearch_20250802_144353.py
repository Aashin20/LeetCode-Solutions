# Last updated: 8/2/2025, 2:43:53 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=-1
        count=0
        for num in nums:
            if count==0:
                ans=num
            if ans==num:
                count+=1
            else:
                count-=1
        return ans