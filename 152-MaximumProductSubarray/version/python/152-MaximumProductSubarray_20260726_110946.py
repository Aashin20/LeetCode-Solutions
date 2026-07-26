# Last updated: 7/26/2026, 11:09:46 AM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        res=max(nums)
4        curMax,curMin=1,1
5        for i in nums:
6            tmp=i*curMax
7            curMax=max(tmp,i*curMin,i)
8            curMin=min(tmp,i*curMin,i)
9            if curMax>res: res=curMax
10        return res