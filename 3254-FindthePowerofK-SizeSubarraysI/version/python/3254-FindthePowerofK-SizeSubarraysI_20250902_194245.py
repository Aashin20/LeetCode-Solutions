# Last updated: 9/2/2025, 7:42:45 PM
from collections import Counter
class Solution:
    def xSum(self,nums,x):
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda x: (x[1], x[0]), reverse=True)
        max_freq = [k*v for k, v in sorted_items[:x]]
        return max_freq

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        l = 0
        for r in range(len(nums)):
            if r-l+1>k:
                l+=1
            if r-l+1==k:
                res.append(sum(self.xSum(nums[l:r+1],x)))
        return res
            
        
