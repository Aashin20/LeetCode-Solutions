# Last updated: 6/14/2025, 10:32:49 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        s=[]
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                s.append(nums[left]**2)
                left+=1
            else:
                s.append(nums[right]**2)
                right-=1
        s.reverse()
        return s